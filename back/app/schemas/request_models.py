from pydantic import BaseModel
from datetime import datetime


class OperacionRequest(BaseModel):
    valor1: float
    valor2: float

class OperacionResponse(BaseModel):
    id: int
    tipo: str
    valor1: float
    valor2: float
    resultado: float
    timestamp: datetime

    class Config:
        from_attributes = True