# Gestão Escolar API

Este projeto é uma API RESTful desenvolvida com **FastAPI** para gerenciar uma escola. Ela permite:

- Cadastro de alunos
- Cadastro de cursos
- Matrículas de alunos nos cursos
- Acompanhamento de notas

## 🚀 Tecnologias utilizadas

- Python
- FastAPI
- Uvicorn
- Docker

## ⚙️ Como executar o projeto

### ▶️ Executar localmente com Uvicorn

```bash
uvicorn app:app --reload

Executar com Docker

docker build -t gestao-escolar-api .
docker run -p 8000:8000 gestao-escolar-api
