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

ENV SUPABASE_URL=https://rhjnjqulvvdtufuedech.supabase.co
ENV SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJoam5qcXVsdnZkdHVmdWVkZWNoIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTcxMTY3MTMsImV4cCI6MjAzMjY5MjcxM30.lq2O4cfI_70hYp6ZF7rrzG-bH9Jcp1Ug-qOuGimqj54

# Exponer el puerto en el que la aplicación correrá
EXPOSE 8000

# Ejecutar la aplicación
CMD ["python", "app/main.py"]
