#!/bin/bash

set -o errexit
set -o nounset

python manage.py collectstatic --noinput
python manage.py migrate
gunicorn --bind 0.0.0.0:8000 notes_manager_project.wsgi:application