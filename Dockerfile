# Usar una imagen base de Python
FROM python:3

# Establecer el directorio de trabajo en /app
WORKDIR /app

# Copiar los archivos de requerimientos al directorio de trabajo
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código de la aplicación al directorio de trabajo
COPY . .

# Exponer el puerto en el que la aplicación correrá
EXPOSE 8000

# Ejecutar la aplicación
CMD ["python", "app/main.py"]
