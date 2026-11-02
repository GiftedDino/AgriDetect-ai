# 🌿 AgriDetect AI --- AI-Based Crop & Pest Disease Detection

> **Detect Early, Protect Crops, Improve Agriculture.**

AgriDetect AI is an AI-powered agricultural platform designed to help
identify crop diseases and pest infestations from plant images. It aims
to make crop-health information more accessible to farmers, agricultural
students, extension workers, and researchers.

🌐 **Live Website:** https://leafscan-ai-y9ob.onrender.com/

------------------------------------------------------------------------

## 📌 Overview

Plant diseases and insect pests can significantly affect crop health and
agricultural productivity. Traditional diagnosis often depends on manual
field observation and expert assessment.

Agridetect AI uses deep-learning-based image analysis to support faster
identification of visible crop-health issues and provide relevant
agricultural information and management recommendations.

The website describes its image-classification approach as **MobileNetV2
transfer learning**, with a PyTorch-based model engine.

## ✨ Features

-   **AI Image Scanner:** Submit a crop, leaf, fruit, or pest image for
    analysis.
-   **Crop Disease Identification:** Classifies supported crop-health
    conditions.
-   **Pest Identification:** Supports identification of selected
    agricultural pests.
-   **Six Diagnostic Categories:**
    1.  Healthy Crop
    2.  Fungal Disease
    3.  Bacterial Disease
    4.  Viral Disease
    5.  Pest Infestation
    6.  Unknown / Unsupported Input
-   **Agricultural Advisory:** Provides information about symptoms,
    causes, and management approaches.
-   **Integrated Pest Management (IPM):** Highlights biological and
    cultural management options.
-   **Crop Information Library:** Provides crop and pathogen
    information.
-   **Field Camera:** Includes a camera-based image capture option.
-   **Weather Risk Information:** Includes information related to
    weather and disease-risk assessment.
-   **Diagnostic Reports:** Supports printable advisory information.

## 🌾 Supported Crops

The website currently lists the following crops and associated examples:

  -----------------------------------------------------------------------
  Crop                    Scientific Name         Examples of listed
                                                  conditions
  ----------------------- ----------------------- -----------------------
  Rice                    *Oryza sativa*          Blast, bacterial leaf
                                                  blight, stem borer

  Wheat                   *Triticum aestivum*     Leaf rust, aphids

  Maize                   *Zea mays*              Fall armyworm

  Tomato                  *Solanum lycopersicum*  Early blight, bacterial
                                                  spot, mosaic virus

  Potato                  *Solanum tuberosum*     Late blight, early
                                                  blight

  Cotton                  *Gossypium hirsutum*    Bacterial blight,
                                                  bollworm, aphids,
                                                  whiteflies

  Apple                   *Malus domestica*       Anthracnose, bitter
                                                  rot, scab

  Grape                   *Vitis vinifera*        Powdery mildew, downy
                                                  mildew, thrips

  Pepper                  *Capsicum annuum*       Thrips, bacterial spot,
                                                  powdery mildew

  Sugarcane               *Saccharum officinarum* Red rot, stem borer

  Groundnut               *Arachis hypogaea*      Tikka (Cercospora leaf
                                                  spot), bollworm

  Soybean                 *Glycine max*           Soybean rust,
                                                  whiteflies
  -----------------------------------------------------------------------

*The exact diseases and pests available for prediction depend on the
model and its supported classes.*

## 🧠 AI & Machine Learning

The website describes the following machine-learning components:

-   **Model approach:** MobileNetV2 transfer learning
-   **Deep-learning framework:** PyTorch (the website displays version
    2.15)
-   **Image classification:** Crop-health and pest-related categories
-   **Input handling:** Confidence-based classification and
    unknown/unsupported-input rejection

### Datasets referenced

The website references these agricultural datasets:

-   **PlantVillage:** Plant leaf images for disease classification.
-   **PlantDoc:** Plant disease images collected in more realistic field
    conditions.
-   **IP102:** Agricultural pest image dataset.

> Dataset references describe the project's stated methodology. They
> should not be interpreted as a claim that every dataset image was used
> to train the currently deployed model.

## ⚙️ How It Works

1.  **Upload an image:** Select or capture an image of a crop, leaf,
    fruit, or pest.
2.  **AI analysis:** The image is processed by the image-classification
    system.
3.  **View the result:** The system returns a predicted diagnostic
    category.
4.  **Explore the advisory:** Review the available symptoms, causes, and
    management recommendations.

## 🎯 Project Objectives

-   Encourage early identification of crop-health problems.
-   Support farmers with accessible agricultural information.
-   Promote awareness of Integrated Pest Management.
-   Reduce unnecessary pesticide use through informed diagnosis.
-   Support agricultural education and research.
-   Explore the practical application of AI in precision agriculture.

## 🌱 Potential Applications

-   Farmers and farming communities
-   Agricultural students
-   Agricultural extension workers
-   Plant pathology education
-   Crop-health monitoring
-   Agricultural research and demonstrations

## 🚀 Getting Started

### Live Demo

Visit the deployed application:

**https://leafscan-ai-y9ob.onrender.com/**

### Run Locally

The public website alone does not expose enough information to verify
the source-code structure, dependencies, or startup command. Once the
project repository is available, replace this section with its actual
installation instructions.

A typical Python project setup may look like this:

``` bash
# Clone your repository
git clone https://github.com/GiftedDino/AgriDetect-ai.git

# Enter the project directory
cd AgriDetect-ai

# Create a virtual environment
python -m venv venv

# Activate the environment (Windows)
venv\Scripts\activate

# Install dependencies (if requirements.txt exists)
pip install -r requirements.txt
```

Add the project's verified run command here after checking its
entry-point file and framework.

## 🛠️ Technology

  Component                          Technology / Approach
  ---------------------------------- ------------------------------------
  AI model                           MobileNetV2
  Learning approach                  Transfer Learning
  Deep-learning framework            PyTorch (as stated on the website)
  Agricultural datasets referenced   PlantVillage, PlantDoc, IP102
  Deployment                         Render (live website URL)

*The website does not independently verify the complete frontend,
backend, database, or deployment configuration. Update this table to
match the source code before publishing.*

## ⚠️ Disclaimer

Agridetect AI is intended as an educational and decision-support tool. AI
predictions may be incorrect, especially when images are unclear or
conditions are outside the supported classes.

Always confirm important crop-health diagnoses with a qualified
agricultural expert or local agricultural extension service before
taking management action. Follow local agricultural recommendations and
pesticide-label instructions.

## 🔮 Future Scope

-   Expand crop and disease coverage.
-   Improve model performance on real-world field images.
-   Add multilingual support for farmers.
-   Improve offline and low-connectivity access.
-   Integrate location-specific agricultural advisories.
-   Expand weather-based disease-risk information.
-   Add more detailed diagnostic history and reporting.

## 👨‍💻 Project

**AgriDetect AI --- AI-Based Crop & Pest Disease Detection System**

Live application: https://leafscan-ai-y9ob.onrender.com/

------------------------------------------------------------------------

```{=html}
<p align="center">
```
`<strong>`{=html}🌿 Detect Early. Protect Crops. Improve
Agriculture.`</strong>`{=html}
```{=html}
</p>
```
⭐ If this project inspires you, consider giving it a star — it motivates future development! 🌱

