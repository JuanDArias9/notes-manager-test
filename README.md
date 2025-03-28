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

> [!WARNING]
> Check Docker is running

### 2. Run the project

```
sh start.sh
```

This will start the application with Docker on http://localhost:8000

### 3. Access the Application

- Open your browser and go to: http://localhost:8000.
- Fill out the form and create new notes.
- View saved notes in the right panel.
- Admin module: http://localhost:8000/admin/

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

> [!NOTE]
> The requirements.txt file is located in the project root.
