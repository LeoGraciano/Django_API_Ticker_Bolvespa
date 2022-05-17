from pathlib import Path
from decouple import config,Csv

import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = config('SECRET_KEY')
DJANGO_SETTINGS_MODULE = config('DJANGO_SETTINGS_MODULE')

DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'index'
AUTH_USER_MODEL = 'accounts.User'

BUSINESS_APPS = [
    'core',
    'accounts',
    'ticker',
]

THIRD_APPS = [

    'fontawesomefree',
    'bootstrap5',
    'celery',
    'django_celery_results',
    'django_celery_beat',

]

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_APPS + BUSINESS_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'plataforma.urls'

MEDIA_URL = config('MEDIA_URL')

MEDIA_ROOT = config('MEDIA_ROOT')


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [''],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

DATABASES = {
    "default": {
        "ENGINE": config('DB_ENGINE'),
        "NAME": config('DB_NAME'),
        "USER": config('DB_USER'),
        "PASSWORD": config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        "PORT": config('DB_PORT')
    }
}
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]



LANGUAGE_CODE = 'pt-br'

DECIMAL_SEPARATOR = ','
USE_THOUSAND_SEPARATOR = True


LANGUAGES = [
    ('pt-br', _('Brazilian Portuguese')),
    ('en', _('English')),
]

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# STATIC_ROOT = config('STATIC_ROOT')
# STATIC_URL = config('STATIC_URL')

# STATICFILES_DIRS = [
#     BASE_DIR / 'static',
# ]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


CELERY_RESULT_BACKEND = 'django-db'
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'America/Sao_Paulo'
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60


EMAIL_BACKEND = config('EMAIL_BACKEND')
EMAIL_USE_SSL = config('EMAIL_USE_SSL')
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_ADMINISTRATOR = config('EMAIL_ADMINISTRATOR')
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_SUPPORT = config('EMAIL_SUPPORT', cast=Csv())
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')
CONTACT_EMAIL = config('CONTACT_EMAIL')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
