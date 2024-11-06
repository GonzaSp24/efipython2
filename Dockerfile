# Dockerfile
FROM python:3.10

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Instalar el paquete cryptography adicionalmente
RUN pip install cryptography

COPY . .

CMD ["flask", "run", "--host=0.0.0.0"]
