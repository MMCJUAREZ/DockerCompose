from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import calculadora_router
from app.database import init_db

app = FastAPI(title="Calculadora API")

# ✅ Middleware CORS correctamente configurado
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # El dominio desde donde accedes
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()

app.include_router(calculadora_router.router, prefix="/operaciones", tags=["operaciones"])
