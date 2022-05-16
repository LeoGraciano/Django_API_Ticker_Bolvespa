
from django.conf  import settings
import os

if settings.DEBUG:

    CELERY_RESULT_BACKEND = 'django-db'

    CELERY_BROKER_URL = 'redis://localhost:6379'
    CELERY_ACCEPT_CONTENT = ['application/json']
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_TASK_SERIALIZER = 'json'

    CELERY_TIMEZONE = 'America/Sao_Paulo'
    CELERY_TASK_TRACK_STARTED = True
    CELERY_TASK_TIME_LIMIT = 30 * 60
else:
    BROKER_URL = BROKER_URL = os.environ.get("REDISCLOUD_URL", "django://")
    BROKER_POOL_LIMIT = 1
    BROKER_CONNECTION_MAX_RETRIES = None

    CELERY_TASK_SERIALIZER = "json"
    CELERY_ACCEPT_CONTENT = ["json", "msgpack"]
    CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'

    if BROKER_URL == "django://":
        settings.INSTALLED_APPS += ("kombu.transport.django",)

    BROKER_TRANSPORT_OPTIONS = {
        "max_connections": 2,
    }
    BROKER_POOL_LIMIT = None