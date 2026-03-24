# rehab-api-core/models/user.py
from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import BaseModel

class UserModel(BaseModel):
    __tablename__ = "users"

    # Multi-Tenant: ¿A qué clínica pertenece este usuario?
    clinic_id = Column(String(36), ForeignKey("clinics.id"), nullable=False)
    
    role = Column(String(50), nullable=False) # ej: "physio", "patient", "admin"
    email = Column(String(150), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    is_active = Column(Boolean, default=True)

    # Relaciones
    clinic = relationship("ClinicModel", back_populates="users")
    patient_profile = relationship("PatientProfileModel", back_populates="user", uselist=False)