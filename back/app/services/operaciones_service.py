from sqlalchemy.orm import Session
from app.models.db_models import Operacion

class OperacionesService:
    def __init__(self, db: Session):
        self.db = db

    def crear_operacion(self, tipo: str, valor1: float, valor2: float, resultado: float):
        operacion = Operacion(
            tipo=tipo,
            valor1=valor1,
            valor2=valor2,
            resultado=resultado
        )
        self.db.add(operacion)
        self.db.commit()
        self.db.refresh(operacion)
        return operacion

    def obtener_historial(self):
        return self.db.query(Operacion).order_by(Operacion.timestamp.desc()).all()