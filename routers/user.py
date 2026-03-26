from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from passlib.context import CryptContext

from db.database import get_db
from models.user import UserModel
from schemas.user import UserCreate, UserResponse

# 1. Configuramos el motor de encriptación (Bcrypt)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

# 2. Creamos el Router
router = APIRouter(
    prefix="/api/users",
    tags=["Users & Authentication"]
)

# 3. Endpoint POST para registrar un usuario
@router.post("/", response_model=UserResponse, status_code=201)
def create_user(user_in: UserCreate, db: Session = Depends(get_db)):
    """
    Registra un nuevo usuario en el sistema (Fisio, Admin o Paciente).
    La contraseña se encripta automáticamente antes de guardarse.
    """
    # Verificamos si el correo ya existe
    user_exists = db.query(UserModel).filter(UserModel.email == user_in.email).first()
    if user_exists:
        raise HTTPException(status_code=400, detail="Este correo ya está registrado.")
    
    # Encriptamos la contraseña en texto plano que llega del Frontend
    hashed_password = get_password_hash(user_in.password)
    
    # Creamos el modelo para la Base de Datos con la clave ya encriptada
    new_user = UserModel(
        email=user_in.email,
        password_hash=hashed_password, 
        first_name=user_in.first_name,
        last_name=user_in.last_name,
        role=user_in.role,
        clinic_id=user_in.clinic_id
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user