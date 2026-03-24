# rehab-api-core/models/clinic.py
from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship

# IMPORTANTE: Importamos nuestra clase maestra que tiene el UUID y las fechas
from db.base_class import BaseModel

class ClinicModel(BaseModel):
    __tablename__ = "clinics"

    # No necesitamos escribir el 'id' ni 'created_at', ¡lo hereda de BaseModel!
    name = Column(String(100), nullable=False)
    subscription_tier = Column(String(50), default="basic")
    is_active = Column(Boolean, default=True)

    # Relaciones (Esto le dice a SQLAlchemy cómo conectarse con otras tablas)
    users = relationship("UserModel", back_populates="clinic")