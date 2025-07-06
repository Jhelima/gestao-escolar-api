from fastapi import APIRouter

matriculas_router = APIRouter()

@matriculas_router.get("/matriculas")
def listar_matriculas():
    return [
        {"id": 1, "aluno": "Maria", "curso": "Python"},
        {"id": 2, "aluno": "João", "curso": "SQL"}
    ]
