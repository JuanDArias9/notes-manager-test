# Notes Manager - HackU Test

A simple web application for creating and listing notes, built with **Django** and **Django REST Framework**.

## Stack

- Python 3
- Django
- Django REST Framework
- Django Forms
- Docker & Docker Compose
- Gunicorn

---

## Installation and Usage

### 1. Clone the repository

```
git clone https://github.com/JuanDArias9/notes-manager-test.git
```

```
cd notes-manager-test
```

### 2. Run the project with Docker (PORT: 8000)

```
docker-compose up --build
```

This will start the application on http://localhost:8000

### 3. Run Migrations

In another terminal, execute:

```
docker-compose exec web python manage.py migrate
```

### 4. Access the Application

- Open your browser and go to: http://localhost:8000.
- Fill out the form and create new notes.
- View saved notes in the right panel.


### Additional information

## Endpoints

```
- Method: GET
- Endpoint: /api/notes/
- Descripción: Get all notes
```

## Stop the container

```
docker-compose down
```

[!NOTE]
the requirements.txt file is located in the project root.
