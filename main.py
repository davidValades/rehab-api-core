from fastapi import FastAPI
from schemas.patient import Patient

app = FastAPI(
    title="rehabGuard API",
    description="API segura para la gestion de historiales de rehabilitacion",
    version="0.0.1",
)

# Endpoint de bienvenida
@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de rehabGuard"}

# Endpoint para crear un nuevo paciente (metodo POST: para enviar informacion nueva)
@app.post("/api/v1/patients/")
def create_patient(patient_data: Patient):
    # Aqui se procesaria la informacion del paciente y se guardaria en la base de datos
    return {
        "message": "Paciente creado exitosamente",
        "patient": patient_data
    }