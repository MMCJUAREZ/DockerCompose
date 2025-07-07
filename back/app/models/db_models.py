from sqlalchemy import Column, Integer, String, Float, DateTime, func
from app.database import Base

class Operacion(Base):
    __tablename__ = "operaciones"

    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String, nullable=False)  # "suma" o "multiplicacion"
    valor1 = Column(Float, nullable=False)
    valor2 = Column(Float, nullable=False)
    resultado = Column(Float, nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())