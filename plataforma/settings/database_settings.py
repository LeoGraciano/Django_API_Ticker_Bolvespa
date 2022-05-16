from pathlib import Path
import os
import dj_database_url
from django.conf import settings

BASE_DIR = Path(__file__).resolve().parent.parent

if settings.DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
        }

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
