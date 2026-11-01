"""Automated Test Suite for AI-Based Crop and Pest Disease Detection System.
Verifies database persistence, model inference, OOD rejection, agronomic service,
and all FastAPI web and REST endpoints.
"""
import sys
import unittest
from pathlib import Path
import torch
from PIL import Image

# Ensure project root is in sys.path
BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from fastapi.testclient import TestClient
from app.main import app
from app.database import init_db, SessionLocal
from app.models.db_models import ScanRecord, AgronomicItem
from app.ml.model_architecture import build_model
from app.ml.classifier import get_classifier
from app.services.agronomy_service import get_agronomy_service


class TestCropDetectionSystem(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        init_db()
        cls.client = TestClient(app)
        cls.classifier = get_classifier()
        cls.agronomy = get_agronomy_service()

    def test_01_database_and_agronomy_seeding(self):
        """Verify database initialized and 27 agronomic profiles are present."""
        items = self.agronomy.get_all_items()
        self.assertGreaterEqual(len(items), 20, "Agronomic database should have at least 20 items.")
        
        # Check specific key classes
        late_blight = self.agronomy.get_by_slug("potato_late_blight")
        self.assertIsNotNone(late_blight)
        self.assertEqual(late_blight["scientific_name"], "Phytophthora infestans")

        armyworm = self.agronomy.get_by_slug("fall_armyworm")
        self.assertIsNotNone(armyworm)
        self.assertEqual(armyworm["scientific_name"], "Spodoptera frugiperda")

    def test_02_model_architecture_forward_pass(self):
        """Verify PyTorch MobileNetV2 architecture accepts standard tensor input."""
        model = build_model(num_classes=26, pretrained=False)
        model.eval()
        dummy_tensor = torch.randn(2, 3, 224, 224)
        with torch.no_grad():
            output = model(dummy_tensor)
        self.assertEqual(output.shape, (2, 26), "Output tensor shape should be (batch_size, num_classes).")

    def test_03_web_pages_load_successfully(self):
        """Verify all HTML views render with 200 OK."""
        routes = ["/", "/detect", "/encyclopedia", "/resources", "/history", "/research"]
        for r in routes:
            response = self.client.get(r)
            self.assertEqual(response.status_code, 200, f"Route {r} failed to load.")
            self.assertIn("AgriDetect", response.text)

    def test_04_weather_risk_calculator(self):
        """Verify epidemiological disease risk calculation under high humidity & cool temperature."""
        response = self.client.post(
            "/api/risk-calculator",
            data={
                "temperature": 18.0,
                "humidity": 92.0,
                "rainfall_mm": 8.0,
                "crop": "Potato"
            }
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["success"])
        # In cool (18C) and 92% humidity with 8mm rain, Late Blight should be Severe
        self.assertEqual(data["data"]["indices"]["late_blight_downy_mildew"], "Severe")

    def test_05_sample_detect_healthy_crop(self):
        """Verify instant detection on pre-loaded healthy rice sample."""
        response = self.client.post("/api/sample-detect/rice_healthy")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["success"])
        self.assertEqual(data["prediction"]["category"], "Healthy Crop")
        self.assertTrue(data["prediction"]["is_healthy"])
        self.assertFalse(data["prediction"]["is_pest"])
        self.assertIn("redirect_url", data)

        record_id = data["record_id"]
        # Verify result page renders for this record
        res_page = self.client.get(f"/result/{record_id}")
        self.assertEqual(res_page.status_code, 200)
        self.assertIn("Rice", res_page.text)

    def test_06_sample_detect_pest_infestation(self):
        """Verify instant detection on fall armyworm sample clearly marks category as Pest Infestation."""
        response = self.client.post("/api/sample-detect/maize_fall_armyworm")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["success"])
        self.assertEqual(data["prediction"]["category"], "Pest Infestation")
        self.assertTrue(data["prediction"]["is_pest"])
        self.assertFalse(data["prediction"]["is_healthy"])
        self.assertEqual(data["prediction"]["scientific_name"], "Spodoptera frugiperda")

    def test_07_sample_detect_ood_unsupported(self):
        """Verify Out-Of-Distribution (OOD) non-crop sample is cleanly classified as Unknown/Unsupported."""
        response = self.client.post("/api/sample-detect/unsupported_object")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["success"])
        self.assertEqual(data["prediction"]["category"], "Unknown or Unsupported Image")
        self.assertTrue(data["prediction"]["is_unknown"])

    def test_08_user_feedback_and_deletion(self):
        """Verify recording user validation feedback and cleaning up test record."""
        # Create a sample record
        res = self.client.post("/api/sample-detect/potato_late_blight")
        record_id = res.json()["record_id"]

        # Submit feedback
        fb_res = self.client.post(f"/api/feedback/{record_id}", data={"feedback": "correct", "notes": "Clear late blight lesions verified"})
        self.assertEqual(fb_res.status_code, 200)
        self.assertTrue(fb_res.json()["success"])

        # Check in DB
        db = SessionLocal()
        rec = db.query(ScanRecord).filter(ScanRecord.id == record_id).first()
        self.assertIsNotNone(rec)
        self.assertEqual(rec.user_feedback, "correct")
        db.close()

        # Delete record
        del_res = self.client.delete(f"/api/history/{record_id}")
        self.assertEqual(del_res.status_code, 200)
        self.assertTrue(del_res.json()["success"])


if __name__ == "__main__":
    unittest.main()

