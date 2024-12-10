#!/bin/bash

echo "Apply database migration"
python manage.py makemigrations
python manage.py migrate

exec "$@"