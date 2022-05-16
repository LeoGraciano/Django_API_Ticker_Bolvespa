web: gunicorn plataforma.wsgi --log-file -
relase: python manage.py collectstatic --noinput
relase: python manage.py makemigrations
relase: python manage.py migrate