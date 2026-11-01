"""MobileNetV2 Transfer Learning Architecture for Crop & Pest Disease Detection.
Academic implementation incorporating depthwise separable convolutions,
dropout regularization, and temperature scaling for calibrated probabilities.
"""
import torch
import torch.nn as nn
from torchvision.models import mobilenet_v2, MobileNet_V2_Weights


class CropPestClassifier(nn.Module):
    """
    MobileNetV2-based Transfer Learning Model for agricultural pathology and entomological classification.
    """
    def __init__(self, num_classes: int = 26, pretrained: bool = True, dropout_rate: float = 0.3):
        super(CropPestClassifier, self).__init__()
        
        # Load backbone
        if pretrained:
            try:
                self.backbone = mobilenet_v2(weights=MobileNet_V2_Weights.DEFAULT)
            except Exception:
                self.backbone = mobilenet_v2(weights=None)
        else:
            self.backbone = mobilenet_v2(weights=None)

        in_features = self.backbone.classifier[1].in_features  # 1280 for MobileNetV2

        # Custom academic classification head with BatchNorm, Dense, LeakyReLU and Dropout
        self.backbone.classifier = nn.Sequential(
            nn.Dropout(p=dropout_rate),
            nn.Linear(in_features, 512),
            nn.BatchNorm1d(512),
            nn.ReLU(inplace=True),
            nn.Dropout(p=dropout_rate * 0.75),
            nn.Linear(512, num_classes)
        )

        # Calibrated temperature parameter for confidence scaling
        self.temperature = nn.Parameter(torch.ones(1) * 1.15)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        logits = self.backbone(x)
        # Apply temperature scaling to soften overconfident predictions on edge inputs
        scaled_logits = logits / self.temperature
        return scaled_logits

    def extract_features(self, x: torch.Tensor) -> torch.Tensor:
        """Extract deep feature embeddings before the final classification head."""
        x = self.backbone.features(x)
        x = nn.functional.adaptive_avg_pool2d(x, (1, 1))
        return torch.flatten(x, 1)


def build_model(num_classes: int = 26, pretrained: bool = True) -> CropPestClassifier:
    """Helper factory for instantiating the neural classifier."""
    model = CropPestClassifier(num_classes=num_classes, pretrained=pretrained)
    return model
