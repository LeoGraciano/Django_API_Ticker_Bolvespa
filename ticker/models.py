from django.utils.translation import ugettext_lazy as _
from django.db import models
from core.models import BaseModelField


class Ticker(BaseModelField):

    logo = models.CharField(_('ID Importação'), max_length=1000, default='')

    name = models.CharField(_('Nome'), max_length=450)

    ticker = models.CharField(_('Ticker'), max_length=10)

    # site = models.CharField(_('Site'), max_length=500, default='')

    close = models.DecimalField(
        _('Preço'), max_digits=10, decimal_places=2, default=0)

    ranges = models.CharField(_('Range'), max_length=350, default="")

    max = models.DecimalField(
        _('Minimo da dia'), max_digits=10, decimal_places=2, default=0)

    min = models.DecimalField(
        _('Maximo do dia'), max_digits=10, decimal_places=2, default=0)

    media = models.DecimalField(
        _('Media do dia'), max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.ticker} - {self.name}"


class HistoricTicker(models.Model):

    ticker = models.ForeignKey(
        'Ticker', related_name='historic_ticker_related',
        on_delete=models.CASCADE
    )

    dt = models.DateTimeField('Data')

    low = models.DecimalField('Min', max_digits=10, decimal_places=2)
    high = models.DecimalField('Max', max_digits=10, decimal_places=2)
    close = models.DecimalField('Preço', max_digits=10, decimal_places=2)
