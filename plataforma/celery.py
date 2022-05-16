from __future__ import absolute_import  # Beacause celery. See: https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html  # noqa: ignore=E501

import os
from celery import Celery, schedules
from django.conf import settings
import sys
from kombu.utils import encoding
sys.modules['celery.utils.encoding'] = encoding

# Load task modules from all registered Django app configs.
# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'plataforma.settings.base')

app = Celery('plataforma')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# Beat Configuração rodar com Celery Comando:
# TODO: Roda Servidor Celery
# celery -A plataforma worker -B -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    # sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')

    # Calls test('world') every 30 seconds
    # sender.add_periodic_task(30.0, test.s('world'), expires=10)

    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        schedules.crontab(hour=0, minute=1, day_of_week=1),
    )


app.conf.beat_schedule = {

    'update_list_ticker': {
        'task': 'ticker.tasks.task_list_ticker',
        'schedule': schedules.crontab(hour='*/30')  # (minute=30, hour='3, 6')
    },
    'task_ticker_update_all': {
        'task': 'ticker.tasks.task_ticker_update_all',
        'schedule': schedules.crontab(hour='*/10')  # (minute=30, hour='3, 6')
    },

}

app.conf.update(BROKER_URL=os.environ['REDIS_URL'],
            CELERY_RESULT_BACKEND=os.environ['REDIS_URL'])