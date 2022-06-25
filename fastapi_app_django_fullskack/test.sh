#!/bin/bash

source ../../bin/activate
python manage.py collectstatic --noinput

uvicorn main:app --reload