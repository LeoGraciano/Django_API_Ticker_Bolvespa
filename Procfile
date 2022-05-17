release: python manage.py makemigrations
release: python manage.py migrate
release: python manage.py collectstatic --noinput
web: gunicorn plataforma.wsgi --log-file -
<<<<<<< HEAD
celery: celery -A plataforma worker -B -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
=======
python manage.py collectstatic --noinput
manage.py migrate
>>>>>>> parent of a298e04... refacto project test
