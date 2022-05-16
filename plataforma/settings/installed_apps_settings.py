

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

