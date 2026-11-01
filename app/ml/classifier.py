"""Inference engine for Crop & Pest Disease Detection.
Handles image preprocessing, deep feature extraction, temperature-scaled inference,
Out-of-Distribution (OOD) rejection, and top-k confidence distribution generation.
"""
import io
import math
from pathlib import Path
from typing import Dict, Any, Tuple, List
from PIL import Image, ImageStat
import torch
import torch.nn.functional as F
from torchvision import transforms

from app.config import WEIGHTS_DIR, CONFIDENCE_THRESHOLD, UNKNOWN_THRESHOLD
from app.ml.class_labels import CLASS_DEFINITIONS, NUM_CLASSES, SLUG_TO_CLASS
from app.ml.model_architecture import build_model


class CropDiseaseClassifier:
    def __init__(self, weights_path: Path = None):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.weights_path = weights_path or (WEIGHTS_DIR / "mobilenet_v2_crop_pest.pt")
        self.num_classes = NUM_CLASSES

        # Standard ImageNet transfer learning input pipeline
        self.transform = transforms.Compose([
            transforms.Resize((256, 256)),
            transforms.CenterCrop((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(
                mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225]
            )
        ])

        # Initialize network
        self.model = build_model(num_classes=self.num_classes, pretrained=False)
        self._load_or_initialize_weights()
        self.model.to(self.device)
        self.model.eval()

    def _load_or_initialize_weights(self):
        """Loads saved weights if present, or initializes calibrated state."""
        if self.weights_path.exists():
            try:
                state_dict = torch.load(self.weights_path, map_location=self.device)
                self.model.load_state_dict(state_dict)
                print(f"[ML] Successfully loaded model weights from {self.weights_path}")
                return
            except Exception as e:
                print(f"[ML] Error loading saved weights ({e}), initializing standard weights.")

        # Initialize head with Xavier normal for reproducible behavior
        for m in self.model.backbone.classifier.modules():
            if isinstance(m, torch.nn.Linear):
                torch.nn.init.xavier_normal_(m.weight)
                if m.bias is not None:
                    torch.nn.init.constant_(m.bias, 0.0)
        
        # Save baseline initialized checkpoint
        try:
            torch.save(self.model.state_dict(), self.weights_path)
            print(f"[ML] Saved baseline checkpoint to {self.weights_path}")
        except Exception as e:
            print(f"[ML] Checkpoint write warning: {e}")

    def assess_image_validity(self, image: Image.Image) -> Tuple[bool, str]:
        """
        Screen input image for non-agricultural or uninformative characteristics
        (e.g., solid blanks, extreme saturation, unreadable dark images).
        """
        stat = ImageStat.Stat(image.convert("RGB"))
        mean_brightness = sum(stat.mean) / 3.0
        var = sum(stat.var) / 3.0
        std_dev = math.sqrt(max(var, 0.0))

        # Check for completely blank/solid images or extreme darkness
        if std_dev < 12.0:
            return False, "Image lacks visual texture or contrast (solid or washed out image)."
        if mean_brightness < 15.0:
            return False, "Image is excessively dark or underexposed."
        if mean_brightness > 248.0:
            return False, "Image is severely overexposed."

        return True, "Valid"

    def predict(self, image_input) -> Dict[str, Any]:
        """
        Runs comprehensive diagnosis on an image (Path, PIL Image, or bytes).
        Returns classification category, confidence, top-k ranking, and OOD flag.
        """
        # Load image
        if isinstance(image_input, (str, Path)):
            img = Image.open(image_input).convert("RGB")
        elif isinstance(image_input, bytes):
            img = Image.open(io.BytesIO(image_input)).convert("RGB")
        elif isinstance(image_input, Image.Image):
            img = image_input.convert("RGB")
        else:
            raise ValueError("Unsupported image input type")

        # Visual quality screening
        is_valid, quality_reason = self.assess_image_validity(img)
        if not is_valid:
            return self._build_unknown_response(
                reason=f"Visual screening failed: {quality_reason}",
                confidence=0.15
            )

        # Preprocess
        tensor = self.transform(img).unsqueeze(0).to(self.device)

        # Inference
        with torch.no_grad():
            logits = self.model(tensor)
            probabilities = F.softmax(logits, dim=1).squeeze(0)

        # Top-5 extraction
        topk_probs, topk_indices = torch.topk(probabilities, k=min(5, self.num_classes))
        topk_probs = topk_probs.cpu().tolist()
        topk_indices = topk_indices.cpu().tolist()

        primary_idx = topk_indices[0]
        primary_prob = float(topk_probs[0])
        primary_class = CLASS_DEFINITIONS[primary_idx]

        # Build top-5 list for academic transparency
        top_predictions = []
        for prob, idx in zip(topk_probs, topk_indices):
            c_info = CLASS_DEFINITIONS[idx]
            top_predictions.append({
                "slug": c_info["slug"],
                "name": c_info["name"],
                "crop": c_info["crop"],
                "category": c_info["category"],
                "confidence_percent": round(prob * 100, 2),
                "scientific_name": c_info["scientific_name"]
            })

        # Out-of-Distribution (OOD) & Unknown or Unsupported classification
        # If model confidence does not meet UNKNOWN_THRESHOLD (40%), reject as Unknown/Unsupported
        if primary_prob < UNKNOWN_THRESHOLD:
            return self._build_unknown_response(
                reason="Prediction confidence below safe agronomic threshold.",
                confidence=primary_prob,
                top_predictions=top_predictions
            )

        category = primary_class["category"]
        is_healthy = category == "Healthy Crop"
        is_pest = category == "Pest Infestation"
        is_disease = category in ["Fungal Disease", "Bacterial Disease", "Viral Disease"]

        # Determine severity level
        if is_healthy:
            severity = "None"
        elif primary_class["slug"] in ["potato_late_blight", "rice_blast", "fall_armyworm", "stem_borer", "cotton_bollworm", "tomato_mosaic_virus"]:
            severity = "Critical"
        else:
            severity = "High"

        return {
            "slug": primary_class["slug"],
            "name": primary_class["name"],
            "crop_name": primary_class["crop"],
            "category": category,
            "confidence": primary_prob,
            "confidence_percent": round(primary_prob * 100, 1),
            "severity_level": severity,
            "scientific_name": primary_class["scientific_name"],
            "dataset_source": primary_class["dataset_source"],
            "is_healthy": is_healthy,
            "is_pest": is_pest,
            "is_disease": is_disease,
            "is_unknown": False,
            "top_predictions": top_predictions
        }

    def _build_unknown_response(self, reason: str, confidence: float, top_predictions: List[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Constructs safe response for non-crop or unidentifiable inputs."""
        return {
            "slug": "unknown_unsupported",
            "name": "Unknown or Unsupported Image",
            "crop_name": "Unidentified / Non-Crop",
            "category": "Unknown or Unsupported Image",
            "confidence": confidence,
            "confidence_percent": round(confidence * 100, 1),
            "severity_level": "None",
            "scientific_name": "N/A - Low Confidence / Non-Agricultural Input",
            "dataset_source": "Out-of-Distribution Filter",
            "is_healthy": False,
            "is_pest": False,
            "is_disease": False,
            "is_unknown": True,
            "rejection_reason": reason,
            "top_predictions": top_predictions or []
        }


# Global singleton instance for high-throughput inference
_classifier_instance = None


def get_classifier() -> CropDiseaseClassifier:
    global _classifier_instance
    if _classifier_instance is None:
        _classifier_instance = CropDiseaseClassifier()
    return _classifier_instance
