# rehab-api-core/schemas/user.py
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime
from uuid import UUID

# 1. Esquema Base (Lo que comparten la creación y la respuesta)
class UserBase(BaseModel):
    email: EmailStr = Field(..., description="Correo electrónico único del usuario")
    first_name: str = Field(..., min_length=2, max_length=100)
    last_name: str = Field(..., min_length=2, max_length=100)
    role: str = Field(..., description="Rol: physio, patient, admin")
    clinic_id: str = Field(..., description="ID de la clínica a la que pertenece (Multi-Tenant)")

# 2. Esquema para CREAR (Lo que envía el Frontend)
class UserCreate(UserBase):
    password: str = Field(..., min_length=8, description="Contraseña en texto plano (se encriptará en el backend)")
    # Fíjate que pedimos 'password' pero tu modelo guarda 'password_hash'. 
    # El servicio (Paso 3) se encargará de esa transformación.

# 3. Esquema de RESPUESTA (Lo que devuelve la API)
class UserResponse(UserBase):
    id: UUID
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True # Permite leer el modelo de SQLAlchemy