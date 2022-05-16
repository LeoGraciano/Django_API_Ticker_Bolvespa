
from nch_capital.utils.validation import isfloat
from decimal import Decimal
import json
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

from django import forms
from core.models import UserVsTicker
from apis.api_rapidapi_brapi import get_ticker
from ticker.models import Ticker
User = get_user_model()


class UserVsTickerForm(forms.Form):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        self.fields['user'].widget = forms.HiddenInput()
        self.fields['ticker'].widget.attrs['list'] = 'datalistOptions'
        if user:
            self.fields['user'].initial = user

    ticker = forms.CharField(label='Empresa', max_length=300)

    user = forms.ModelChoiceField(label='Cliente', queryset=User.objects.all())

    class Meta:
        fields = ['user', 'ticker']

    def clean_user(self):
        user = self.cleaned_data.get('user')
        if not user:
            raise forms.ValidationError('Usuário não existe')

        return user

    def clean_ticker(self):
        ticker = self.cleaned_data.get('ticker')
        response = get_ticker(ticker)
        if response.status_code != 200:
            tk = Ticker.objects.filter(ticker=ticker)
            if not tk.exists():
                raise forms.ValidationError(
                    f"CODE: {response.status_code}: Ticker {ticker.upper()}, não Encontrado")
            return tk[0]

        ticker = ticker.upper()
        json_data = json.loads((response.text).replace(
            'yield', 'media'))

        ticker_data = {}

        for k, v in json_data.items():
            if hasattr(Ticker, k.lower()) or v:
                if ',' in v and isfloat(v):
                    v = Decimal(v.replace(',', '.'))

                ticker_data[k.lower()] = v

        ticker = Ticker.objects.update_or_create(
            ticker=ticker,
            defaults=ticker_data
        )[0]

        return ticker

    def save(self):
        user = self.cleaned_data.get('user')
        tk = self.cleaned_data.get('ticker')
        uvt = UserVsTicker.objects.get(user=user.pk)
        uvt.ticker.add(tk)

        return uvt
