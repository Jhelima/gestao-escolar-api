# Gestão Escolar API

# 📚 Gestão Escolar API

Este é um projeto de API escolar desenvolvido como parte dos meus estudos em Engenharia de Software. A aplicação tem como objetivo realizar o **cadastro de alunos, cursos, matrículas e notas** de forma simples e organizada.

---

## 🚀 Funcionalidades

- Cadastro de alunos
- Cadastro de cursos
- Matrícula de alunos em cursos
- Registro de notas
- Visualização de todos os dados via endpoints REST

---

## 🛠 Tecnologias Utilizadas

- **Python 3.10**
- **FastAPI**
- **Uvicorn**
- **Docker**

---

## ⚙️ Como executar o projeto

> Antes de tudo, é necessário ter o **Python 3.10** e o **Docker** instalados.

### 1. Clone o repositório:

```bash
git clone https://github.com/Jhelima/gestao-escolar-api.git
cd gestao-escolar-api

Crie um ambiente virtual e ative:
python3 -m venv venv
source venv/bin/activate

 Instale as dependências:
 pip install -r requirements.txt

Execute a API localmente:
uvicorn main:app --reload

 Acesse no navegador:
 http://127.0.0.1:8000/docs
 
 🐳 Executar com Docker
 docker build -t minha-app-fastapi .
docker run -p 8000:8000 minha-app-fastapi

💡 Sobre o Projeto
Este projeto foi desenvolvido no curso da Alura em parceria com Google Cloud, com o objetivo de mover uma aplicação local para a nuvem. Aqui pude praticar:

Estruturação de uma API REST com FastAPI

Organização em rotas e modelos

Containerização com Docker

Boas práticas com README e versionamento no GitHub