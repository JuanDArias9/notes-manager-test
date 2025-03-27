FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
COPY ./start.sh /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start
# Puerto en el que corre Django (8000 por defecto)
EXPOSE 8000