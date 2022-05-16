web: gunicorn plataforma.wsgi --log-file -
python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate