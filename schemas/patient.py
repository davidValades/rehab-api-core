from pydantic import BaseModel

class Patient(BaseModel):
    id: int
    name: str
    age: int
    injury: str
    is_active: bool = True