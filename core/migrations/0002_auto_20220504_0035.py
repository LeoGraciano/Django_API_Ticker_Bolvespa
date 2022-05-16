# Generated by Django 3.2 on 2022-05-04 03:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0004_ticker'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uservsticker',
            name='ticker',
        ),
        migrations.AddField(
            model_name='uservsticker',
            name='ticker',
            field=models.ManyToManyField(related_name='user_vs_ticker_related', to='ticker.Ticker', verbose_name='Ticker'),
        ),
        migrations.AlterField(
            model_name='uservsticker',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_vs_ticker_related', to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
    ]
