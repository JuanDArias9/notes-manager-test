FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Puerto en el que corre Django (8000 por defecto)
EXPOSE 8000

# CMD para ejecutar la aplicación
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "notas.wsgi:application"]