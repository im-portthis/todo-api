#!/usr/bin/env bash

export DJANGO_SETTINGS_MODULE=project.settings

if [[ ${DJANGO_STATIC} = 1 ]]; then
    python manage.py collectstatic --noinput
fi

if [[ ${DJANGO_MIGRATE} = 1 ]]; then
    if [[ ${POSTGRES_HOST} != "" ]]; then
        echo "Waiting 11.11s. for database..."
        sleep 11.11
        echo "Database started"
    fi
    python manage.py migrate
fi

if [[ ${DJANGO_WEB} = 1 ]]; then
    if [[ ${DEBUG} = 1 ]]; then
        echo "Starting debug server..."
        python manage.py runserver 0.0.0.0:8000 --noreload
    else
        echo "Server not run!"
        echo "TODO: ... "
    fi
fi
