from fastapi import FastAPI
from schemas.patient import Patient # Este es el de Pydantic (esquema)
from db.database import engine, Base
from models.patient import PatientModel # Este es el de SQLAlchemy (modelo)

# Crear las tablas
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="RehabGuard API",
    description="API segura para la gestión de historiales de rehabilitación",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de RehabGuard"}

@app.post("/api/v1/patients")
def create_patient(patient_data: Patient):
    return {
        "message": "Paciente registrado con éxito",
        "data": patient_data
    }