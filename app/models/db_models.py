from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, Float, Text, DateTime, Boolean
from app.database import Base


def utc_now():
    return datetime.now(timezone.utc)


class ScanRecord(Base):
    __tablename__ = "scan_records"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String(255), nullable=False)
    image_path = Column(String(512), nullable=False)
    crop_name = Column(String(100), nullable=True)
    diagnosis_name = Column(String(150), nullable=False)
    category = Column(String(50), nullable=False)  # Healthy Crop, Fungal Disease, etc.
    is_healthy = Column(Boolean, default=False)
    is_pest = Column(Boolean, default=False)
    is_disease = Column(Boolean, default=False)
    confidence = Column(Float, nullable=False)
    severity_level = Column(String(30), default="Moderate")  # Low, Moderate, High, Severe, None
    scientific_name = Column(String(150), nullable=True)
    symptoms_summary = Column(Text, nullable=True)
    top_predictions_json = Column(Text, nullable=True)  # JSON string of top-5
    user_feedback = Column(String(50), nullable=True)   # "correct", "incorrect"
    user_notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=utc_now, index=True)

    def to_dict(self):
        return {
            "id": self.id,
            "filename": self.filename,
            "image_path": self.image_path,
            "crop_name": self.crop_name,
            "diagnosis_name": self.diagnosis_name,
            "category": self.category,
            "is_healthy": self.is_healthy,
            "is_pest": self.is_pest,
            "is_disease": self.is_disease,
            "confidence": round(self.confidence, 2),
            "severity_level": self.severity_level,
            "scientific_name": self.scientific_name,
            "symptoms_summary": self.symptoms_summary,
            "user_feedback": self.user_feedback,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S") if self.created_at else None
        }


class AgronomicItem(Base):
    __tablename__ = "agronomic_items"

    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String(100), unique=True, index=True)
    name = Column(String(150), nullable=False)
    scientific_name = Column(String(150), nullable=True)
    category = Column(String(50), nullable=False)  # Healthy Crop, Fungal, Bacterial, Viral, Pest
    crop_name = Column(String(100), nullable=True)
    affected_crops = Column(Text, nullable=True)
    affected_parts = Column(String(150), nullable=True)
    symptoms = Column(Text, nullable=True)
    causes_biology = Column(Text, nullable=True)
    encouraging_conditions = Column(Text, nullable=True)
    spread_mechanism = Column(Text, nullable=True)
    ipm_recommendations = Column(Text, nullable=True)
    biological_control = Column(Text, nullable=True)
    cultural_control = Column(Text, nullable=True)
    chemical_management = Column(Text, nullable=True)
    prevention_methods = Column(Text, nullable=True)
    reference_dataset = Column(String(100), default="PlantVillage / IP102")


class FarmerInquiry(Base):
    __tablename__ = "farmer_inquiries"

    id = Column(Integer, primary_key=True, index=True)
    farmer_name = Column(String(100), nullable=False)
    contact_info = Column(String(150), nullable=False)
    crop_type = Column(String(100), nullable=False)
    inquiry_text = Column(Text, nullable=False)
    created_at = Column(DateTime, default=utc_now)
