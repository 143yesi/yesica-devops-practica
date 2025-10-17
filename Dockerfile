# Imagen base de Python
FROM python:3.11

# Carpeta de trabajo dentro del contenedor
WORKDIR /app

# Copiar archivos del proyecto al contenedor
COPY . /app

# Instalar dependencias si tienes un requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Comando para ejecutar tu aplicación
CMD ["python", "main.py"]
