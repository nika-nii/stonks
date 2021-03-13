#!/bin/bash

# echo "Collect static files"
# python manage.py collectstatic --noinput

echo "Apply database migrations"
python manage.py migrate

echo "Creating superuser"
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell

echo "Starting server"
python manage.py runserver 0.0.0.0:80