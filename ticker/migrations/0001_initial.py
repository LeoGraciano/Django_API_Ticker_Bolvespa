# Generated by Django 3.2 on 2022-05-17 12:44

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticker',
            fields=[
                ('code', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='created_at', verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, db_column='updated_at', verbose_name='Aualizado em')),
                ('logo', models.CharField(default='', max_length=1000, verbose_name='ID Importação')),
                ('name', models.CharField(max_length=450, verbose_name='Nome')),
                ('ticker', models.CharField(max_length=10, verbose_name='Ticker')),
                ('close', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Preço')),
                ('ranges', models.CharField(default='', max_length=350, verbose_name='Range')),
                ('max', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Minimo da dia')),
                ('min', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Maximo do dia')),
                ('media', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Media do dia')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HistoricTicker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateTimeField(verbose_name='Data')),
                ('low', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Min')),
                ('high', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Max')),
                ('close', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preço')),
                ('ticker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historic_ticker_related', to='ticker.ticker')),
            ],
        ),
    ]
