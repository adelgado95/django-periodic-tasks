#!/bin/bash

sudo docker exec -it project-db psql -U postgres -c  "SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE pid <> pg_backend_pid() AND datname = 'project';"
sudo docker exec -it project-db psql -U postgres -c  "DROP DATABASE project;"
sudo docker exec -it project-db psql -U postgres -c  "CREATE DATABASE project;"

sudo docker exec project-admin python manage.py makemigrations categorias
sudo docker exec project-admin python manage.py makemigrations
sudo docker exec project-admin python manage.py migrate django_celery_beat
sudo docker exec project-admin python manage.py migrate

sudo docker exec project-admin python manage.py loaddata db_data/auth_user.json
sudo docker exec project-admin python manage.py loaddata db_data/dcelery_periodict_tasks.json
sudo docker exec project-admin python manage.py loaddata db_data/djcelery_crontab_schedule.json
