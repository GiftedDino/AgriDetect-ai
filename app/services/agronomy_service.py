"""Agronomy Knowledge Service & Weather-driven Epidemiological Risk Calculator.
Supplies verified phytopathological and entomological data and computes
real-time sporulation risk based on ambient meteorological variables.
"""
import json
from pathlib import Path
from typing import Dict, Any, List, Optional
from sqlalchemy.orm import Session

from app.config import DATA_DIR
from app.models.db_models import AgronomicItem


class AgronomyService:
    def __init__(self):
        self.db_path = DATA_DIR / "agronomy_db.json"
        self._data_cache: Dict[str, Any] = {}
        self._load_cache()

    def _load_cache(self):
        if self.db_path.exists():
            with open(self.db_path, "r", encoding="utf-8") as f:
                self._data_cache = json.load(f)

    def get_all_items(self) -> List[Dict[str, Any]]:
        return list(self._data_cache.values())

    def get_by_slug(self, slug: str) -> Optional[Dict[str, Any]]:
        return self._data_cache.get(slug)

    def search_items(self, query: str = "", category: str = "", crop: str = "") -> List[Dict[str, Any]]:
        query = query.lower().strip()
        category = category.lower().strip()
        crop = crop.lower().strip()

        results = []
        for item in self._data_cache.values():
            # Filter by category
            if category and category != "all" and category not in item.get("category", "").lower():
                continue
            # Filter by crop
            if crop and crop != "all" and crop not in item.get("crop_name", "").lower():
                continue
            # Filter by text search
            if query:
                searchable = (
                    item.get("name", "") + " " +
                    item.get("scientific_name", "") + " " +
                    item.get("crop_name", "") + " " +
                    item.get("symptoms", "")
                ).lower()
                if query not in searchable:
                    continue
            results.append(item)
        return results

    def seed_database_if_empty(self, db: Session):
        """Populates the database agronomic_items table if empty."""
        count = db.query(AgronomicItem).count()
        if count == 0 and self._data_cache:
            for slug, item in self._data_cache.items():
                db_item = AgronomicItem(
                    slug=slug,
                    name=item.get("name"),
                    scientific_name=item.get("scientific_name"),
                    category=item.get("category"),
                    crop_name=item.get("crop_name"),
                    affected_crops=", ".join(item.get("affected_crops", [])),
                    affected_parts=item.get("affected_parts"),
                    symptoms=item.get("symptoms"),
                    causes_biology=item.get("causes_biology"),
                    encouraging_conditions=item.get("encouraging_conditions"),
                    spread_mechanism=item.get("spread_mechanism"),
                    ipm_recommendations=item.get("ipm_recommendations"),
                    biological_control=item.get("biological_control"),
                    cultural_control=item.get("cultural_control"),
                    chemical_management=item.get("chemical_management"),
                    prevention_methods=item.get("prevention_methods")
                )
                db.add(db_item)
            db.commit()
            print(f"[AgronomyService] Seeded {len(self._data_cache)} items to database.")

    def calculate_epidemiological_risk(
        self,
        temperature: float,
        humidity: float,
        rainfall_mm: float = 0.0,
        crop: str = "General"
    ) -> Dict[str, Any]:
        """
        Calculates pathogen sporulation and pest outbreak risk indices based on
        established microclimatic threshold models (Wallin, Blitecast, Mills).
        """
        # 1. Late Blight / Oomycete Risk (Cool & wet)
        late_blight_risk = "Low"
        if 13.0 <= temperature <= 22.0 and humidity >= 85.0:
            if rainfall_mm > 5.0 or humidity >= 92.0:
                late_blight_risk = "Severe"
            else:
                late_blight_risk = "High"
        elif 10.0 <= temperature <= 25.0 and humidity >= 75.0:
            late_blight_risk = "Moderate"

        # 2. Rice Blast / Fungal Leaf Spot (Warm & humid)
        rice_blast_risk = "Low"
        if 20.0 <= temperature <= 28.0 and humidity >= 88.0:
            rice_blast_risk = "Severe" if rainfall_mm > 2.0 else "High"
        elif 18.0 <= temperature <= 32.0 and humidity >= 78.0:
            rice_blast_risk = "Moderate"

        # 3. Bacterial Leaf Blight & Spot (High heat & wetness/rain)
        bacterial_blight_risk = "Low"
        if 25.0 <= temperature <= 35.0 and humidity >= 80.0:
            if rainfall_mm > 5.0:
                bacterial_blight_risk = "Severe"
            else:
                bacterial_blight_risk = "High"
        elif 22.0 <= temperature <= 36.0 and humidity >= 70.0:
            bacterial_blight_risk = "Moderate"

        # 4. Sucking Pests (Aphids, Thrips, Whiteflies) - warm & dry
        sucking_pest_risk = "Low"
        if 24.0 <= temperature <= 36.0 and humidity <= 60.0 and rainfall_mm == 0.0:
            sucking_pest_risk = "Severe"
        elif 20.0 <= temperature <= 34.0 and humidity <= 70.0:
            sucking_pest_risk = "High"
        elif 18.0 <= temperature <= 30.0:
            sucking_pest_risk = "Moderate"

        # General Composite Advisory
        advisories = []
        if late_blight_risk in ["High", "Severe"]:
            advisories.append("High risk for Late Blight / Downy Mildew. Apply prophylactic protectant fungicide (Mancozeb or Copper hydroxide) before rain events.")
        if rice_blast_risk in ["High", "Severe"]:
            advisories.append("Environmental conditions favor Blast & Leaf Spot sporulation. Delay nitrogen top-dressing and scout panicle/flag leaves.")
        if bacterial_blight_risk in ["High", "Severe"]:
            advisories.append("Bacterial Blight risk elevated. Avoid sprinkler irrigation and avoid handling wet crop foliage to prevent bacterial spread.")
        if sucking_pest_risk in ["High", "Severe"]:
            advisories.append("Warm dry conditions trigger rapid multiplication of aphids, thrips, and whiteflies. Inspect lower leaf undersides and install yellow/blue sticky cards.")

        if not advisories:
            advisories.append("Current ambient conditions represent Low overall pathogen pressure. Maintain routine IPM scouting.")

        return {
            "inputs": {
                "temperature": temperature,
                "humidity": humidity,
                "rainfall_mm": rainfall_mm,
                "crop": crop
            },
            "indices": {
                "late_blight_downy_mildew": late_blight_risk,
                "rice_blast_foliar_fungi": rice_blast_risk,
                "bacterial_blight_spot": bacterial_blight_risk,
                "sucking_pests_outbreak": sucking_pest_risk
            },
            "advisories": advisories
        }


# Singleton service
_agronomy_service = None


def get_agronomy_service() -> AgronomyService:
    global _agronomy_service
    if _agronomy_service is None:
        _agronomy_service = AgronomyService()
    return _agronomy_service
