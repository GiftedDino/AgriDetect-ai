"""Application Runner for AI-Based Crop and Pest Disease Detection System.
Launches the FastAPI Uvicorn server on http://127.0.0.1:8000
"""
import sys
import uvicorn
from pathlib import Path

# Configure utf-8 console output for Windows compatibility
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Add project root to sys.path
BASE_DIR = Path(__file__).resolve().parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

if __name__ == "__main__":
    print("=" * 75)
    print(">> Starting AI-Based Crop and Pest Disease Detection System...")
    print(">> Web Server running on: http://127.0.0.1:8000")
    print(">> Academic Research Docs: http://127.0.0.1:8000/research")
    print(">> Crop & Pest Compendium: http://127.0.0.1:8000/encyclopedia")
    print(">> Extension & Weather:   http://127.0.0.1:8000/resources")
    print("=" * 75)

    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=8000,
        reload=False,
        log_level="info"
    )
