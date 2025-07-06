from fastapi import APIRouter

cursos_router = APIRouter()

@cursos_router.get("/cursos")
def listar_cursos():
    return [
        {"id": 1, "nome": "FastAPI para Iniciantes"},
        {"id": 2, "nome": "Banco de Dados com SQLAlchemy"}
    ]
