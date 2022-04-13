#!/bin/sh

cd jsuite && python manage.py runserver 8080 &
cd jsuite-frontend && npm start
