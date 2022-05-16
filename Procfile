web: gunicorn --pythonpath nch_capital nch_capital.wsgi --log-file -
python manage.py collectstatic --noinput
manage.py migrate