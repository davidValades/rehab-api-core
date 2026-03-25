from fastapi import APIRouter

# Creamos el "enrutador" y le damos un prefijo para que todas sus URLs empiecen igual
router = APIRouter(
    prefix="/api/patients",
    tags=["Patients"]
)

@router.post("/")
def create_patient():
    
    return {"mensaje": "Recurso creado"}