#!/bin/sh

echo "Waiting for Database..."

# while ! nc -z django_db 3306; do
#   sleep 1
# done

# cd bizzydataoperation

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# # Start server
echo "Starting server"
# python manage.py runserver 0.0.0.0:8000
gunicorn -b 0.0.0.0:8000 rtrw_serpong.wsgi