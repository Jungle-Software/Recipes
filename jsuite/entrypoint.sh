#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

sed -i 's/force_text/force_str/g' '/usr/local/lib/python3.9/site-packages/graphene_django/utils/utils.py'
#python manage.py flush --no-input
python manage.py migrate

exec "$@"