from sqlalchemy import Column, Integer, String, Boolean
from db.database import Base

# Clase que representa la tabla "patients" en la base de datos
class PatientModel(Base):
    # nombre de la tabla en la base de datos
    __tablename__ = "patients"

    # Definimos las columnas
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    injury = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    
