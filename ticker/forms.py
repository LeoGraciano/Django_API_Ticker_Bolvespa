from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

from .models import Ticker


from django import forms


class TickerForm(forms.Form):
    class Meta:
        model = Ticker
        fields = '__all__'
