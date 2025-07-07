from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.request_models import OperacionRequest, OperacionResponse
from app.services.operaciones_service import OperacionesService
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/sumar", response_model=OperacionResponse)
def sumar(datos: OperacionRequest, db: Session = Depends(get_db)):
    resultado = datos.valor1 + datos.valor2
    operacion = OperacionesService(db).crear_operacion("suma", datos.valor1, datos.valor2, resultado)
    return operacion

@router.post("/multiplicar", response_model=OperacionResponse)
def multiplicar(datos: OperacionRequest, db: Session = Depends(get_db)):
    resultado = datos.valor1 * datos.valor2
    operacion = OperacionesService(db).crear_operacion("multiplicacion", datos.valor1, datos.valor2, resultado)
    return operacion

@router.get("/historial", response_model=list[OperacionResponse])
def historial(db: Session = Depends(get_db)):
    return OperacionesService(db).obtener_historial()