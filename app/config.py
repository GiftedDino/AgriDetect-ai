import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Paths
APP_DIR = BASE_DIR / "app"
STATIC_DIR = BASE_DIR / "static"
UPLOAD_DIR = STATIC_DIR / "uploads"
SAMPLE_DIR = APP_DIR / "data" / "sample_images"
TEMPLATES_DIR = BASE_DIR / "templates"
DATA_DIR = APP_DIR / "data"
WEIGHTS_DIR = APP_DIR / "ml" / "weights"

# Ensure runtime directories exist
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
SAMPLE_DIR.mkdir(parents=True, exist_ok=True)
WEIGHTS_DIR.mkdir(parents=True, exist_ok=True)

# Database
DATABASE_URL = f"sqlite:///{BASE_DIR / 'crop_detection.db'}"

# ML Configuration
MODEL_ARCH = "mobilenet_v2"  # "mobilenet_v2" or "efficientnet_b0"
CONFIDENCE_THRESHOLD = 0.55  # Minimum confidence threshold for valid prediction
UNKNOWN_THRESHOLD = 0.40     # Below this, classified as Unknown/Unsupported Image
MAX_UPLOAD_SIZE_MB = 15

# Supported Categories
CATEGORIES = {
    "HEALTHY": "Healthy Crop",
    "FUNGAL": "Fungal Disease",
    "BACTERIAL": "Bacterial Disease",
    "VIRAL": "Viral Disease",
    "PEST": "Pest Infestation",
    "UNKNOWN": "Unknown or Unsupported Image"
}
