# rehab-api-core/schemas/patient.py
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime
from uuid import UUID

# 1. Esquema Base (Lo que comparten la creación y la respuesta)
class PatientBase(BaseModel):
    email: EmailStr = Field(..., description="Correo electrónico único del paciente")
    first_name: str = Field(..., min_length=2, max_length=100)
    last_name: str = Field(..., min_length=2, max_length=100)
    role: str = Field(..., description="Rol: physio, patient, admin")
    clinic_id: str = Field(..., description="ID de la clínica a la que pertenece (Multi-Tenant)")
    injury: str= Field(..., min_length=2, max_length=255)
    medical_history: Optional[str] = Field(None)
    age: int = Field(...)

# 2. Esquema para CREAR (Lo que envía el Frontend)
class PatientCreate(PatientBase):
    pass

# 3. Esquema de RESPUESTA (Lo que devuelve la API)
class PatientResponse(PatientBase):
    id: UUID
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True # Permite leer el modelo de SQLAlchemy