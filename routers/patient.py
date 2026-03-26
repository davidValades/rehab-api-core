from fastapi import APIRouter
from schemas.patient import PatientCreate, PatientResponse

# Creamos el "enrutador" y le damos un prefijo para que todas sus URLs empiecen igual
router = APIRouter(
    prefix="/api/patients",
    tags=["Patients"]
)

@router.post("/")
def create_patient(patient: PatientCreate):
    return {"mensaje": "Paciente validado correctamente", "datos_recibidos": patient}
