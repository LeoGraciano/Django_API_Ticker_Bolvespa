from decouple import Csv, config

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

