# Imagen base
FROM python:3.10-slim

# Directorio de trabajo
WORKDIR /app

# Copiar archivos
COPY . .

# Instalar dependencias (si tienes requirements.txt)
# RUN pip install -r requirements.txt

# Comando por defecto
CMD ["python", "main.py"]