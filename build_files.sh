#!/bin/bash

# Instala pip si no está disponible
python3 -m ensurepip --upgrade || python -m ensurepip --upgrade

# Instala las dependencias desde requirements.txt
python3 -m pip install -r requirements.txt || python -m pip install -r requirements.txt

# Recopila archivos estáticos
python3 manage.py collectstatic --noinput || python manage.py collectstatic --noinput
