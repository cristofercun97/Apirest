# Imagen base
FROM python:3.11

# Crear directorio de la aplicación
WORKDIR /app

# Copiar los archivos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Exponer el puerto
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
