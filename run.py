"""Application Runner for AI-Based Crop and Pest Disease Detection System.
Launches the FastAPI Uvicorn server locally or on cloud platforms (Render, Railway).
"""
import os
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
    # Dynamically detect port from environment (Render / Railway inject PORT, defaults to 8000 locally)
    port = int(os.environ.get("PORT", 8000))
    host = "0.0.0.0" if os.environ.get("PORT") else "127.0.0.1"

    print("=" * 75)
    print(f">> Starting AI-Based Crop and Pest Disease Detection System...")
    print(f">> Web Server running on: http://{host}:{port}")
    print(f">> Academic Research Docs: http://{host}:{port}/research")
    print(f">> Crop & Pest Compendium: http://{host}:{port}/encyclopedia")
    print(f">> Extension & Weather:   http://{host}:{port}/resources")
    print("=" * 75)

    uvicorn.run(
        "app.main:app",
        host=host,
        port=port,
        reload=False,
        log_level="info"
    )
