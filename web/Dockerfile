# Usar a imagem oficial do Python
FROM python:3.9-slim

# Definir o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiar o arquivo de dependências
COPY requirements.txt requirements.txt

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante da aplicação
COPY . .

# Expôr a porta 5000 (onde a aplicação Flask roda)
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "app.py"]
