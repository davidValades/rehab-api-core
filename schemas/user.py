# rehab-api-core/schemas/user.py
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime
from uuid import UUID

# 1. Esquema Base (Datos comunes de cualquier usuario del sistema)
class UserBase(BaseModel):
    email: EmailStr = Field(..., description="Correo electrónico único del usuario")
    first_name: str = Field(..., min_length=2, max_length=100)
    last_name: str = Field(..., min_length=2, max_length=100)
    role: str = Field(..., description="Rol: physio, patient, admin")
    clinic_id: UUID = Field(..., description="ID de la clínica a la que pertenece (Multi-Tenant)")

# 2. Esquema para CREAR (Lo que envía el Frontend al registrarse)
# En schemas/user.py
class UserCreate(UserBase):
    password: str = Field(
        ..., 
        min_length=8, 
        max_length=72, 
        description="Contraseña del usuario (máximo 72 caracteres para Bcrypt)"
    )
# 3. Esquema de RESPUESTA (Lo que devolvemos al Frontend)
class UserResponse(UserBase):
    id: UUID
    is_active: bool
    created_at: datetime
    # Fíjate que NO devolvemos el password aquí. ¡Seguridad por diseño!

    class Config:
        from_attributes = True