from django import template
from django.db.models import Exists, OuterRef, Q, Count, F, Max, Sum

import locale


register = template.Library()


@register.filter(name='money')
def money_br(value):
    if value:
        locale.setlocale(locale.LC_ALL, 'pt_BR')
        return locale.currency(value, grouping=True)
    return value
