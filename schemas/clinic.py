# rehab-api-core/schemas/clinic.py
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from uuid import UUID


class ClinicBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100, description="Nombre de la clínica")
    email: str = Field(..., description="Correo de contacto de la clínica")


class ClinicCreate(ClinicBase):
    pass 


class ClinicResponse(ClinicBase):
    id: UUID 
    created_at: datetime
    
    class Config:
        from_attributes = True 