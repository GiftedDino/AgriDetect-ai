# AI-Based Crop and Pest Disease Detection System Using Artificial Intelligence and Machine Learning

> **Tagline:** *"Detect Early, Protect Crops, Improve Agriculture."*

[![Python](https://img.shields.io/badge/Python-3.14-blue.svg)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.15-orange.svg)](https://pytorch.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.162-teal.svg)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/Academic-Research%20License-green.svg)]()

A complete academic and agricultural research-grade web application integrating deep transfer learning (MobileNetV2), an agronomic scientific knowledge base, live field camera diagnostics, real-time epidemiological weather risk simulation, and full database persistence.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Key Features](#key-features)
3. [Diagnostic Categories](#diagnostic-categories)
4. [Supported Crops, Pathologies & Pests](#supported-crops-pathologies--pests)
5. [AI & Machine Learning Architecture](#ai--machine-learning-architecture)
6. [System Architecture](#system-architecture)
7. [Installation & Setup](#installation--setup)
8. [Running the Application](#running-the-application)
9. [Automated Test Suite](#automated-test-suite)
10. [Academic References](#academic-references)

---

## 1. Project Overview

Plant diseases and insect infestations compromise 20% to 40% of global agricultural production annually (FAO). Traditional diagnostic methods require experienced plant pathologists or laboratory culturing, which are inaccessible in remote rural regions. 

This platform bridges cutting-edge computer vision with agronomic science by delivering:
- **Instant Image Classification:** Analyzes photographs of crop leaves, stems, fruits, and insect pests.
- **Strict Pathology Categorization:** Differentiates fungal, bacterial, viral, and entomological conditions, while actively rejecting non-plant and unconfident inputs using an **Out-Of-Distribution (OOD)** filter.
- **Scientific Advisory Dossiers:** Provides scientific names (e.g., *Phytophthora infestans*, *Spodoptera frugiperda*), pathogen etiology, environmental triggers, and Integrated Pest Management (IPM) multi-tier recommendations.
- **Weather-Driven Sporulation Risk Calculator:** Computes microclimatic pathogen pressure based on local temperature and relative humidity.

---

## 2. Key Features

### 🌾 1. Landing Page
- Modern agricultural responsive UI designed with high-contrast accessibility.
- Project tagline and academic background.
- Direct navigation buttons: **Detect Disease**, **Explore Crops**, **Agricultural Resources**.
- Illustrated **3-Step Workflow** (Upload $\to$ AI Analysis $\to$ Agronomic Advisory).
- Live model status indicator and supported crop gallery.

### 🔬 2. AI Crop and Pest Detection Module
- **Input Channels:**
  - Drag-and-drop zone.
  - Device file browser (supports JPG, PNG, WEBP).
  - Live webcam streaming with front/rear camera toggle and snapshot preview.
- **One-Click Demonstration Specimens:** Instant testing for Rice Healthy, Potato Late Blight, Tomato Early Blight, Cotton Aphids, Maize Fall Armyworm, Rice Bacterial Leaf Blight, and Non-Crop OOD objects.
- **Laser Scanner Animation:** Multi-step visual progress display showing tensor conversion, InvertedResidual feature extraction, temperature-scaled softmax, and agronomic mapping.
- **Real-Time Diagnostic Card:** Displays host crop, disease/pest name, confidence percentage, category badge, and link to printable advisory report.

### 📋 3. Detailed Diagnostic Result & Advisory Page
- **Scientific Binomial & Taxonomy:** Pathogen/pest Latin names and biological orders.
- **Top-5 Model Probability Distribution:** Calibrated softmax ranking for academic transparency.
- **Comprehensive Agronomic Tabs:**
  1. *Symptoms & Visible Damage*
  2. *Causes, Biology & Environmental Favorability*
  3. *Integrated Pest Management (IPM):* Biological Control, Cultural Control, and Targeted Chemical Guidance.
  4. *Proactive Prevention & Farmer Action Checklist*
- **Printable Advisory Sheet:** Formatted for extension agents and smallholders.
- **Validation Feedback Mechanism:** Allows farmers and students to rate diagnosis accuracy.

### 📚 4. Crop, Disease & Pest Encyclopedia
- Interactive directory covering 12 economic crops, 14 diseases, and 10 pests.
- Real-time search by common name, crop, symptoms, or scientific pathogen name.
- Filter by category (*All, Healthy, Fungal, Bacterial, Viral, Pest*) and host crop.
- Modal dialogs providing complete phytopathological profiles.

### ☁️ 5. Extension Resources & Meteorological Risk Simulator
- **Microclimatic Disease Risk Calculator:** Simulates pathogen sporulation (Late Blight, Rice Blast, Bacterial Blight, Sucking Pests) from ambient temperature, humidity, and rainfall.
- **Global Agricultural Repositories:** Direct links to FAO, CABI PlantwisePlus, ICAR, USDA ARS, CGIAR (IRRI, CIMMYT, CIP), and APSnet.
- **Agronomic Helpline Form:** Farmer and student field inquiry submission backed by SQLite persistence.

### 📊 6. Scan History & Database Analytics
- Local SQLite database logging scan timestamp, image path, crop, diagnosis, category, confidence, and validation feedback.
- Real-time statistical analytics cards (Total Scans, Healthy %, Fungal %, Bacterial %, Pest %, OOD %).
- Historical search, individual report review, and record deletion.

### 🎓 7. Academic Research Documentation
- Comprehensive thesis-grade documentation covering the mathematical foundations of MobileNetV2 depthwise separable convolutions, transfer learning rationale, dataset harmonization, evaluation metrics, and peer-reviewed citations.

---

## 3. Diagnostic Categories

To ensure scientific validity and avoid misdiagnoses, the system separates classifications into six strict categories:

| Category | Description | Representative Examples |
| :--- | :--- | :--- |
| **A. Healthy Crop** | Clean foliar tissue with optimal photosynthetic vigor | Rice Healthy, Potato Healthy, Tomato Healthy, Grape Healthy |
| **B. Fungal Disease** | Spores, mycelia, concentric rings, pustules, powdery mats | Early Blight (*Alternaria solani*), Late Blight (*P. infestans*), Rice Blast |
| **C. Bacterial Disease** | Water-soaked lesions, bacterial ooze, angular spots | Bacterial Leaf Blight (*X. oryzae*), Bacterial Spot, Black Arm |
| **D. Viral Disease** | Systemic mosaic mottling, shoe-stringing, stunting | Tomato Yellow Leaf Curl Virus (TYLCV), Tomato Mosaic Virus (ToMV) |
| **E. Pest Infestation** | Foliar rasping, window-paning, bore holes, honeydew | Fall Armyworm (*S. frugiperda*), Cotton Aphids, Rice Stem Borer |
| **F. Unknown / Unsupported** | Non-crop objects, extreme blur, low statistical confidence | Rejects non-agricultural photos below the 55% threshold |

---

## 4. Supported Crops, Pathologies & Pests

### Supported Crops (12)
1. **Rice** (*Oryza sativa*)
2. **Wheat** (*Triticum aestivum*)
3. **Maize** (*Zea mays*)
4. **Tomato** (*Solanum lycopersicum*)
5. **Potato** (*Solanum tuberosum*)
6. **Cotton** (*Gossypium hirsutum*)
7. **Apple** (*Malus domestica*)
8. **Grape** (*Vitis vinifera*)
9. **Pepper** (*Capsicum annuum*)
10. **Sugarcane** (*Saccharum officinarum*)
11. **Groundnut** (*Arachis hypogaea*)
12. **Soybean** (*Glycine max*)

### Key Agricultural Pests Supported (10)
- **Cotton & Green Peach Aphids** (*Aphis gossypii* / *Myzus persicae*)
- **Fall Armyworm** (*Spodoptera frugiperda*)
- **Whiteflies** (*Bemisia tabaci*)
- **Yellow Rice Stem Borer** (*Scirpophaga incertulas*)
- **Cotton / American Bollworm** (*Helicoverpa armigera*)
- **Chilli & Onion Thrips** (*Scirtothrips dorsalis*)
- **Serpentine Leaf Miner** (*Liriomyza trifolii*)
- **Cutworms & Tobacco Caterpillars** (*Spodoptera litura*)
- **Oriental Fruit Flies** (*Bactrocera dorsalis*)
- **Mealybugs** (*Phenacoccus solenopsis*)

### Key Pathologies Supported (14+)
- **Early Blight** (*Alternaria solani*)
- **Late Blight** (*Phytophthora infestans*)
- **Rice Blast** (*Magnaporthe oryzae*)
- **Bacterial Leaf Blight** (*Xanthomonas oryzae pv. oryzae*)
- **Grape Powdery Mildew** (*Erysiphe necator*)
- **Grape Downy Mildew** (*Plasmopara viticola*)
- **Wheat Leaf Rust** (*Puccinia triticina*)
- **Apple Anthracnose & Bitter Rot** (*Colletotrichum gloeosporioides*)
- **Tomato Bacterial Spot** (*Xanthomonas campestris pv. vesicatoria*)
- **Cotton Bacterial Blight / Black Arm** (*Xanthomonas citri pv. malvacearum*)
- **Tomato Yellow Leaf Curl & Mosaic Virus**
- **Groundnut Tikka / Cercospora Leaf Spot** (*Cercospora arachidicola*)
- **Sugarcane Red Rot** (*Colletotrichum falcatum*)
- **Soybean Rust** (*Phakopsora pachyrhizi*)

---

## 5. AI & Machine Learning Architecture

### Model Architecture
- **Backbone:** MobileNetV2 with pre-trained ImageNet feature weights.
- **Inverted Residual Blocks:** Depthwise separable convolutions with expansion factor $t=6$.
- **Custom Classification Head:**
  - `Dropout(p=0.30)`
  - `Linear(1280, 512)`
  - `BatchNorm1d(512)`
  - `ReLU(inplace=True)`
  - `Dropout(p=0.225)`
  - `Linear(512, 26)`
- **Temperature Scaling Calibration:** Calibrated parameter $T=1.15$ softening overconfident out-of-distribution logits:
  $$P(y = c \mid x) = \frac{\exp(z_c / T)}{\sum_{j=1}^{K} \exp(z_j / T)}$$

### Training & Evaluation Pipeline (`app/ml/train_eval.py`)
1. **Dataset Ingestion:** Stratified sampling representing PlantVillage, PlantDoc, and IP102 spectral distributions.
2. **Data Augmentation:**
   - `RandomResizedCrop(224, scale=(0.8, 1.0))`
   - `RandomHorizontalFlip(p=0.5)`
   - `RandomRotation(degrees=20)`
   - `ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2)`
3. **Loss & Optimization:** Cross-Entropy Loss with AdamW ($\text{lr}=10^{-3}$, $\text{weight\_decay}=10^{-4}$) and Cosine Annealing Learning Rate scheduling.
4. **Metrics:** Generates multiclass confusion matrix, precision, recall, and macro F1-score.

---

## 6. System Architecture

```
[ User Browser / Mobile Camera ]
              │
              ▼
   [ FastAPI REST Backend (Uvicorn) ]
   ├── Static Files Mount (/static)
   ├── Jinja2 Template Engine (/templates)
   ├── SQLite Database (crop_detection.db)
   │
   ├── [ ML Inference Engine (PyTorch) ]
   │    ├── Torchvision Transforms
   │    ├── MobileNetV2 Inverted Residual Backbone
   │    ├── Temperature-Scaled Softmax
   │    └── Out-of-Distribution (OOD) Filter
   │
   └── [ Agronomy Knowledge Service ]
        ├── 27 Scientific Disease/Pest Dossiers
        ├── Weather Epidemiological Risk Calculator
        └── Formatted Advisory Sheet Generator
```

---

## 7. Installation & Setup

### Prerequisites
- Python 3.10+ (Tested on Python 3.14.3)
- Windows, macOS, or Linux

### 1. Clone or Open Workspace
```powershell
cd "d:\Crop detection"
```

### 2. Install Dependencies
```powershell
pip install -r requirements.txt
```

---

## 8. Running the Application & Connecting Frontend and Backend

### How Frontend and Backend Are Connected

The platform utilizes a **high-performance unified full-stack architecture** built on FastAPI:

* **Backend Engine (`app/`):**
  * Asynchronous REST API endpoints (`/api/detect`, `/api/sample-detect`, `/api/risk-calculator`, `/api/feedback`).
  * PyTorch MobileNetV2 deep neural network inference pipeline (`app/ml/classifier.py`).
  * SQLite database (`crop_detection.db`) managed via SQLAlchemy ORM.
* **Frontend Client (`templates/` & `static/`):**
  * Jinja2 HTML5 responsive views (`index.html`, `detect.html`, `result.html`, `encyclopedia.html`, `resources.html`, `history.html`).
  * Interactive JavaScript controller ([`static/js/main.js`](file:///d:/Crop%20detection/static/js/main.js)) managing drag-and-drop file ingestion, camera webcam streaming (`MediaDevices.getUserMedia`), and laser scan animation.
  * JavaScript uses asynchronous `fetch('/api/detect')` and `fetch('/api/sample-detect/{slug}')` calls to communicate seamlessly with the backend.

Because FastAPI hosts both the static frontend assets and the backend API on the same origin (`http://127.0.0.1:8000`), **frontend and backend are connected automatically with zero CORS configuration required.**

---

### PowerShell Commands to Launch & Connect

#### Method 1: Standard Production Runner (Recommended)
Open PowerShell and enter:

```powershell
# 1. Navigate to project root directory
cd "d:\Crop detection"

# 2. Launch unified application server
python run.py
```

*Output:*
```
>> Starting AI-Based Crop and Pest Disease Detection System...
>> Web Server running on: http://127.0.0.1:8000
>> Academic Research Docs: http://127.0.0.1:8000/research
>> Crop & Pest Compendium: http://127.0.0.1:8000/encyclopedia
>> Extension & Weather:   http://127.0.0.1:8000/resources
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

Now open your browser and navigate to: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

#### Method 2: Development Mode with Live Auto-Reload
If you are modifying templates or Python code and want changes to reload instantly without restarting:

```powershell
cd "d:\Crop detection"
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

---

#### Method 3: Verify Frontend-to-Backend Connection via PowerShell
To verify that the backend REST API is actively responding to frontend requests, open a second PowerShell terminal and run:

```powershell
# 1. Verify frontend web interface response
Invoke-WebRequest -Uri "http://127.0.0.1:8000/" -UseBasicParsing

# 2. Test instant AI diagnosis API (specimen: Healthy Rice)
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/sample-detect/rice_healthy" -Method Post

# 3. Test microclimatic weather risk calculator API
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/risk-calculator" -Method Post -Body @{
    temperature = 21.5
    humidity = 92
    rainfall_mm = 6.0
    crop = "Potato"
}
```

---

### Application Endpoint Directory

Once the PowerShell command is running, access all features directly:

| Page / Component | URL | Connected Backend Handlers |
| :--- | :--- | :--- |
| **Home Landing Page** | [http://127.0.0.1:8000](http://127.0.0.1:8000) | `GET /` |
| **AI Disease & Pest Detector** | [http://127.0.0.1:8000/detect](http://127.0.0.1:8000/detect) | `POST /api/detect`, `POST /api/sample-detect/{slug}` |
| **Diagnostic Result Dossier** | [http://127.0.0.1:8000/result/{id}](http://127.0.0.1:8000/result/1) | `GET /result/{record_id}`, `POST /api/feedback/{record_id}` |
| **Crop & Pest Encyclopedia** | [http://127.0.0.1:8000/encyclopedia](http://127.0.0.1:8000/encyclopedia) | `GET /encyclopedia`, `GET /api/encyclopedia/item/{slug}` |
| **Extension & Weather Risk** | [http://127.0.0.1:8000/resources](http://127.0.0.1:8000/resources) | `POST /api/risk-calculator`, `POST /api/inquiry` |
| **Scan History & Analytics** | [http://127.0.0.1:8000/history](http://127.0.0.1:8000/history) | `GET /history`, `DELETE /api/history/{record_id}` |
| **Interactive OpenAPI Docs** | [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) | Swagger UI for testing all backend API endpoints |
| **Academic ML Research** | [http://127.0.0.1:8000/research](http://127.0.0.1:8000/research) | `GET /research` |

---

### Train or Retrain the AI Model
To execute the complete 9-step training, evaluation, and metric generation pipeline:
```powershell
python app/ml/train_eval.py
```

---

## 9. Automated Test Suite

Run the comprehensive unit and integration tests:
```powershell
python -m unittest tests/test_app.py
```

The test suite validates:
- ✅ Database schema creation & agronomic profile seeding.
- ✅ MobileNetV2 forward pass & tensor dimensions.
- ✅ All web view routes return HTTP 200 OK.
- ✅ Meteorological risk calculation under high humidity conditions.
- ✅ Healthy crop sample detection.
- ✅ Pest infestation diagnosis and scientific naming.
- ✅ Out-of-Distribution (OOD) rejection for non-crop samples.
- ✅ User feedback submission and record management.

---

## 10. Academic References

1. **Sandler, M., Howard, A., Zhu, M., Zhmoginov, A., & Chen, L. C. (2018).** *MobileNetV2: Inverted Residuals and Linear Bottlenecks.* IEEE/CVF CVPR, 4510–4520.
2. **Hughes, D. P., & Salathé, M. (2015).** *An open access repository of images on plant health to enable the development of mobile disease diagnostics.* arXiv:1511.08060 (PlantVillage).
3. **Singh, D., et al. (2020).** *PlantDoc: a dataset for visual plant disease detection in the wild.* ACM IKDD CoDS-COMAD, 249–253.
4. **Wu, X., et al. (2019).** *IP102: A Large-Scale Benchmark Dataset for Insect Pest Recognition.* IEEE/CVF CVPR, 8787–8796.
5. **Food and Agriculture Organization (FAO). (2021).** *The Impact of Disasters and Crises on Agriculture and Food Security: Plant Pests and Diseases.* Rome, Italy.

---

## 11. GitHub Repository Setup & Publishing Reference

Follow these steps to publish this project to your GitHub account:

### Step 1: Create an Empty Repository on GitHub
1. Log in to [GitHub](https://github.com/).
2. In the top-right corner, click **`+`** $\to$ **New repository**.
3. **Repository name:** `crop-disease-detection` *(or any preferred name)*.
4. **Description:** `AI-Based Crop and Pest Disease Detection System using Deep Learning (MobileNetV2) and FastAPI.`
5. Choose **Public** or **Private**.
6. **Do NOT** check *"Add a README file"*, *"Add .gitignore"*, or *"Choose a license"* (the repository already contains customized versions of these).
7. Click **Create repository**.
8. Copy the repository URL (e.g., `https://github.com/YOUR_USERNAME/crop-disease-detection.git`).

---

### Step 2: Configure Git Identity in PowerShell
If you have not set up your Git username and email on this machine yet, run:

```powershell
# Set your Git username and email (replace with your actual name and email)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

---

### Step 3: Commit and Push Code to GitHub
Run the following commands in PowerShell from the project folder:

```powershell
# 1. Navigate to project root
cd "d:\Crop detection"

# 2. Stage all files (respecting .gitignore)
git add .

# 3. Create your initial commit
git commit -m "feat: initial commit for AI crop and pest disease detection system"

# 4. Ensure branch is named 'main'
git branch -M main

# 5. Link to your GitHub remote repository (replace YOUR_USERNAME and REPO_NAME)
git remote add origin https://github.com/YOUR_USERNAME/crop-disease-detection.git

# 6. Push your code to GitHub
git push -u origin main
```

---

### Step 4: Making Future Updates
Whenever you modify files or retrain models, update your GitHub repository with:

```powershell
git add .
git commit -m "feat: describe your recent changes"
git push
```


