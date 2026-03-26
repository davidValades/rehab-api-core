# rehab-api-core/main.py
from fastapi import FastAPI
from db.database import engine, Base

# 1. Importar TODOS los modelos antes de create_all
from models.clinic import ClinicModel
from models.user import UserModel
from models.patient import PatientProfileModel

# 2. Importamos nuestros Routers
from routers import clinic, patient

# 3. Crear todas las tablas en la Base de Datos
Base.metadata.create_all(bind=engine)

# 4. Inicializar FastAPI con la nueva visión SaaS
app = FastAPI(
    title="RehabGuard API | B2B SaaS",
    description="Motor Backend seguro para la gestión Multi-Tenant de clínicas de rehabilitación.",
    version="2.0.0"
)

# 5. Conectar los routers a la aplicación principal
app.include_router(clinic.router)
app.include_router(patient.router)

# 6. Endpoint de salud (Health Check)
@app.get("/", tags=["Health"])
def read_root():
    return {
        "status": "online",
        "message": "Bienvenido a RehabGuard API. Sistema Multi-Tenant activado. 🚀"
    }