from fastapi import APIRouter

alunos_router = APIRouter()

@alunos_router.get("/alunos")
def listar_alunos():
    return [{"id": 1, "nome": "Maria"}, {"id": 2, "nome": "João"}]
