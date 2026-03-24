# rehab-api-core/models/patient.py
from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship

from db.base_class import BaseModel

class PatientProfileModel(BaseModel):
    __tablename__ = "patient_profiles"

    # Conectamos este perfil clínico con la cuenta de usuario (login) y la clínica
    user_id = Column(String(36), ForeignKey("users.id"), nullable=False, unique=True)
    clinic_id = Column(String(36), ForeignKey("clinics.id"), nullable=False)

    # Tus campos clínicos
    age = Column(Integer, nullable=False)
    injury = Column(String(255), nullable=False)
    medical_history = Column(Text, nullable=True) # Campo amplio para el historial

    # Relaciones
    user = relationship("UserModel", back_populates="patient_profile")