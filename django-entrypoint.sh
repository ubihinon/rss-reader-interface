#!/bin/bash

python manage.py migrate
python manage.py collectstatic --noinput
python manage.py compilemessages
python db-entrypoint.py

python manage.py runserver 0.0.0.0:80
