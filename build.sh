#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Only run migrations if DATABASE_URL is set
if [ ! -z "$DATABASE_URL" ]; then
    python manage.py migrate --noinput
fi