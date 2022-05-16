
from uuid import uuid4

from django.db import models
from django.utils.translation import ugettext_lazy as _

class BaseModelField(models.Model):
    """Classe de composição para modelos que utilizaram os
        campos created_at, updated_at
    """
    code = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(
        _('Criado em'), auto_now_add=True,
        db_column='created_at'
    )
    updated_at = models.DateTimeField(
        _('Aualizado em'), auto_now=True,
        db_column='updated_at'
    )

    class Meta:
        abstract = True


class UserVsTicker(BaseModelField):

    user = models.OneToOneField(
        'accounts.User', related_name='user_vs_ticker_related',
        verbose_name=_('Usuário'), on_delete=models.CASCADE
    )

    ticker = models.ManyToManyField(
        'ticker.Ticker', verbose_name=_('Ticker'),
        related_name='user_vs_ticker_related'
    )

    def __str__(self):
        return f'{self.user.name} - Ticker: {self.ticker.count()}'
