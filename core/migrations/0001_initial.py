# Generated by Django 3.2 on 2022-05-16 19:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ticker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserVsTicker',
            fields=[
                ('code', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='created_at', verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, db_column='updated_at', verbose_name='Aualizado em')),
                ('ticker', models.ManyToManyField(related_name='user_vs_ticker_related', to='ticker.Ticker', verbose_name='Ticker')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_vs_ticker_related', to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
