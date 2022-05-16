# Mini projeto para NHC Capital

Projeto solicitado pelo Gestor Pedro da NCH Capital

# Necessário realizar primeiro migrate

python manage.py makemigrations && python manage.py migrate

# Sincronica do lista Ticker necessário rodar o servidor do Celery e ter servidor redis ativos

celery==5.2.6
django_celery_results==2.3.1
django_celery_beat==2.2.1

## Comando roda Celery

celery -A plataforma worker -B -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
