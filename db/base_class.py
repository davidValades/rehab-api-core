# rehab-api-core/db/base_class.py
import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, DateTime, String

# IMPORTANTE: Importamos la Base que creamos en database.py
from db.database import Base 

class BaseModel(Base):
    """
    Clase abstracta maestra. 
    Todas las tablas de nuestra base de datos heredarán de aquí.
    Garantiza que toda tabla tenga un UUID seguro, fecha de creación y Soft Deletes.
    """
    __abstract__ = True # Le dice a SQLAlchemy que no cree una tabla llamada 'BaseModel'

    # 1. Identificador único seguro: UUIDv4 como clave primaria
    id = Column(
        String(36), 
        primary_key=True, 
        index=True, 
        default=lambda: str(uuid.uuid4())
    )

    # 2. Trazabilidad: Fecha de creación con zona horaria UTC
    created_at = Column(
        DateTime(timezone=True), 
        default=lambda: datetime.now(timezone.utc)
    )

    # 3. Soft Deletes: Campo para marcar registros como eliminados sin borrarlos físicamente
    deleted_at = Column(
        DateTime(timezone=True), 
        nullable=True, 
        default=None
    )