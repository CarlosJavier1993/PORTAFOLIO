#!/bin/bash

# Instala pip si no está disponible
python -m ensurepip --upgrade || python -m ensurepip --upgrade

# Instala las dependencias desde requirements.txt
python -m pip install -r requirements.txt || python -m pip install -r requirements.txt

# Recopila archivos estáticos
python manage.py collectstatic --noinput || python manage.py collectstatic --noinput
