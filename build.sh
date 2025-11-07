#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Collect static files (without database connection)
DJANGO_SETTINGS_MODULE=neeraali_backend.settings python manage.py collectstatic --noinput --clear