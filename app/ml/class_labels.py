"""Class definitions and taxonomy mappings for AI Crop & Pest Detection."""

CLASS_DEFINITIONS = [
    {
        "id": 0,
        "slug": "tomato_early_blight",
        "name": "Tomato Early Blight",
        "crop": "Tomato",
        "category": "Fungal Disease",
        "scientific_name": "Alternaria solani",
        "dataset_source": "PlantVillage"
    },
    {
        "id": 1,
        "slug": "potato_late_blight",
        "name": "Potato Late Blight",
        "crop": "Potato",
        "category": "Fungal Disease",
        "scientific_name": "Phytophthora infestans",
        "dataset_source": "PlantVillage"
    },
    {
        "id": 2,
        "slug": "rice_blast",
        "name": "Rice Blast",
        "crop": "Rice",
        "category": "Fungal Disease",
        "scientific_name": "Magnaporthe oryzae",
        "dataset_source": "PlantDoc"
    },
    {
        "id": 3,
        "slug": "grape_powdery_mildew",
        "name": "Grape Powdery Mildew",
        "crop": "Grape",
        "category": "Fungal Disease",
        "scientific_name": "Erysiphe necator",
        "dataset_source": "PlantVillage"
    },
    {
        "id": 4,
        "slug": "grape_downy_mildew",
        "name": "Grape Downy Mildew",
        "crop": "Grape",
        "category": "Fungal Disease",
        "scientific_name": "Plasmopara viticola",
        "dataset_source": "PlantVillage"
    },
    {
        "id": 5,
        "slug": "wheat_leaf_rust",
        "name": "Wheat Leaf Rust",
        "crop": "Wheat",
        "category": "Fungal Disease",
        "scientific_name": "Puccinia triticina",
        "dataset_source": "PlantDoc"
    },
    {
        "id": 6,
        "slug": "apple_anthracnose",
        "name": "Apple Anthracnose & Bitter Rot",
        "crop": "Apple",
        "category": "Fungal Disease",
        "scientific_name": "Colletotrichum gloeosporioides",
        "dataset_source": "PlantVillage"
    },
    {
        "id": 7,
        "slug": "groundnut_tikka_disease",
        "name": "Groundnut Tikka (Cercospora Leaf Spot)",
        "crop": "Groundnut",
        "category": "Fungal Disease",
        "scientific_name": "Cercospora arachidicola",
        "dataset_source": "PlantDoc"
    },
    {
        "id": 8,
        "slug": "sugarcane_red_rot",
        "name": "Sugarcane Red Rot",
        "crop": "Sugarcane",
        "category": "Fungal Disease",
        "scientific_name": "Colletotrichum falcatum",
        "dataset_source": "PlantDoc"
    },
    {
        "id": 9,
        "slug": "rice_bacterial_leaf_blight",
        "name": "Rice Bacterial Leaf Blight",
        "crop": "Rice",
        "category": "Bacterial Disease",
        "scientific_name": "Xanthomonas oryzae",
        "dataset_source": "PlantDoc"
    },
    {
        "id": 10,
        "slug": "tomato_bacterial_spot",
        "name": "Tomato Bacterial Spot",
        "crop": "Tomato",
        "category": "Bacterial Disease",
        "scientific_name": "Xanthomonas campestris pv. vesicatoria",
        "dataset_source": "PlantVillage"
    },
    {
        "id": 11,
        "slug": "cotton_bacterial_blight",
        "name": "Cotton Bacterial Blight (Black Arm)",
        "crop": "Cotton",
        "category": "Bacterial Disease",
        "scientific_name": "Xanthomonas citri pv. malvacearum",
        "dataset_source": "PlantDoc"
    },
    {
        "id": 12,
        "slug": "tomato_mosaic_virus",
        "name": "Tomato Mosaic & Yellow Leaf Curl Virus",
        "crop": "Tomato",
        "category": "Viral Disease",
        "scientific_name": "Tomato Yellow Leaf Curl Virus / ToMV",
        "dataset_source": "PlantVillage"
    },
    {
        "id": 13,
        "slug": "aphids_infestation",
        "name": "Cotton & Green Peach Aphids",
        "crop": "Cotton",
        "category": "Pest Infestation",
        "scientific_name": "Aphis gossypii / Myzus persicae",
        "dataset_source": "IP102"
    },
    {
        "id": 14,
        "slug": "fall_armyworm",
        "name": "Fall Armyworm (FAW)",
        "crop": "Maize",
        "category": "Pest Infestation",
        "scientific_name": "Spodoptera frugiperda",
        "dataset_source": "IP102"
    },
    {
        "id": 15,
        "slug": "whiteflies_infestation",
        "name": "Whiteflies Infestation",
        "crop": "Cotton",
        "category": "Pest Infestation",
        "scientific_name": "Bemisia tabaci",
        "dataset_source": "IP102"
    },
    {
        "id": 16,
        "slug": "stem_borer",
        "name": "Yellow Rice Stem Borer",
        "crop": "Rice",
        "category": "Pest Infestation",
        "scientific_name": "Scirpophaga incertulas",
        "dataset_source": "IP102"
    },
    {
        "id": 17,
        "slug": "cotton_bollworm",
        "name": "Cotton / American Bollworm",
        "crop": "Cotton",
        "category": "Pest Infestation",
        "scientific_name": "Helicoverpa armigera",
        "dataset_source": "IP102"
    },
    {
        "id": 18,
        "slug": "thrips_infestation",
        "name": "Chilli & Onion Thrips",
        "crop": "Pepper",
        "category": "Pest Infestation",
        "scientific_name": "Scirtothrips dorsalis",
        "dataset_source": "IP102"
    },
    {
        "id": 19,
        "slug": "leaf_miners",
        "name": "Serpentine Leaf Miner",
        "crop": "Tomato",
        "category": "Pest Infestation",
        "scientific_name": "Liriomyza trifolii",
        "dataset_source": "IP102"
    },
    {
        "id": 20,
        "slug": "rice_healthy",
        "name": "Rice (Healthy)",
        "crop": "Rice",
        "category": "Healthy Crop",
        "scientific_name": "Oryza sativa",
        "dataset_source": "PlantVillage"
    },
    {
        "id": 21,
        "slug": "tomato_healthy",
        "name": "Tomato (Healthy)",
        "crop": "Tomato",
        "category": "Healthy Crop",
        "scientific_name": "Solanum lycopersicum",
        "dataset_source": "PlantVillage"
    },
    {
        "id": 22,
        "slug": "potato_healthy",
        "name": "Potato (Healthy)",
        "crop": "Potato",
        "category": "Healthy Crop",
        "scientific_name": "Solanum tuberosum",
        "dataset_source": "PlantVillage"
    },
    {
        "id": 23,
        "slug": "maize_healthy",
        "name": "Maize (Healthy)",
        "crop": "Maize",
        "category": "Healthy Crop",
        "scientific_name": "Zea mays",
        "dataset_source": "PlantVillage"
    },
    {
        "id": 24,
        "slug": "cotton_healthy",
        "name": "Cotton (Healthy)",
        "crop": "Cotton",
        "category": "Healthy Crop",
        "scientific_name": "Gossypium hirsutum",
        "dataset_source": "PlantVillage"
    },
    {
        "id": 25,
        "slug": "grape_healthy",
        "name": "Grape (Healthy)",
        "crop": "Grape",
        "category": "Healthy Crop",
        "scientific_name": "Vitis vinifera",
        "dataset_source": "PlantVillage"
    }
]

SLUG_TO_CLASS = {item["slug"]: item for item in CLASS_DEFINITIONS}
NUM_CLASSES = len(CLASS_DEFINITIONS)
