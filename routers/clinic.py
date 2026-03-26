# rehab-api-core/routers/clinic.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from db.database import get_db
from models.clinic import ClinicModel
from schemas.clinic import ClinicCreate, ClinicResponse

# Creamos el Router (agrupador de rutas)
router = APIRouter(
    prefix="/api/clinics",
    tags=["Clinics (Multi-Tenant)"]
)

# Endpoint POST para crear una clínica
@router.post("/", response_model=ClinicResponse, status_code=201)
def create_clinic(clinic_in: ClinicCreate, db: Session = Depends(get_db)):
    """
    Crea una nueva clínica en el sistema SaaS.
    """
    clinica_existe = db.query(ClinicModel).filter(ClinicModel.email == clinic_in.email).first()
    if clinica_existe:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Ya existe una clínica con ese correo.")    
    
    # 1. Transformamos el dato validado de Pydantic al Modelo de SQLAlchemy
    new_clinic = ClinicModel(
        name=clinic_in.name,
        email=clinic_in.email,
        subscription_tier=clinic_in.subscription_tier,
        is_active=clinic_in.is_active
    )
    
    # 2. Guardamos en la base de datos
    db.add(new_clinic)
    db.commit()             # Confirmamos la transacción
    db.refresh(new_clinic)  # Refrescamos para obtener el UUID generado y la fecha

    return new_clinic

# Endpoint GET para obtener todas las clínicas
@router.get("/", response_model=List[ClinicResponse])
def get_clinics(db: Session = Depends(get_db)):
    """
    Obtiene una lista de todas las clínicas registradas en el sistema SaaS.
    """
    clinics = db.query(ClinicModel).all()
    return clinics