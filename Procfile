release: python manage.py makemigrations
release: python manage.py migrate
web: gunicorn plataforma.wsgi --log-file -
celery: celery -A plataforma worker -B -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler