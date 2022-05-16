web: gunicorn plataforma.wsgi --log-file -
release: python manage.py collectstatic --noinput
release: python manage.py makemigrations
release: python manage.py migrate