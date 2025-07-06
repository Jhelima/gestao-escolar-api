# Usar imagem oficial do Python
FROM python:3.10-slim

# Diretório de trabalho
WORKDIR /app

# Copia os arquivos para dentro do container
COPY . .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta que o Uvicorn usará
EXPOSE 8000

# Comando para rodar a API
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
