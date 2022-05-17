from __future__ import absolute_import, unicode_literals
from datetime import datetime
from decimal import Decimal
from celery import shared_task
import pytz
from apis.api_rapidapi_brapi import get_ticker, list_ticker
import json
from django.utils import timezone
from utils.validation import isfloat

from .models import HistoricTicker, Ticker


@shared_task(timeout=800000)
def task_list_ticker():
    response = list_ticker()

    list_data = json.loads((response.text).replace(
        '"stock"', '"ticker"'))

    for _k, _v in list_data.items():
        for _ in _v:
            objs_data = _.copy()
            ticker = ''
            for k, v in _.items():
                ticker = objs_data.pop('ticker', None)
                if not hasattr(Ticker, k):
                    objs_data.pop(k)
                elif isfloat(v):
                    objs_data[v] = Decimal(v.replace(',', '.'))

            if ticker:
                Ticker.objects.update_or_create(
                    ticker=ticker,
                    defaults=objs_data
                )


@shared_task(timeout=800000)
def task_ticker_update_all(list_tk=None):
    if Ticker.objects.all().exists():
        if not list_tk:
            list_tk = (str(list(Ticker.objects.all().values_list(
                'ticker', flat=True).distinct()))).replace('[', '',).replace(']', '',).replace("'", "").replace(" ", "").replace("None", "").replace(",,", ",")
        else:
            list_tk = (str(list(list_tk))).replace('[', '',).replace(']', '',).replace(
                "'", "").replace(" ", "").replace("None", "").replace(",,", ",")
        response = get_ticker(list_tk)

        if response.status_code != 200:
            return False

        list_data = json.loads((response.text).replace(
            'symbol', 'ticker'))

        for _k, _v in list_data.items():
            for _ in _v:
                if type(_) is dict:
                    objs_data = _.copy()
                    ticker = ''
                    for k, v in _.items():
                        if not _.get('ticker', None):
                            continue
                        if k == "ticker":
                            ticker = objs_data.pop('ticker')
                        elif k == "longName":
                            objs_data['name'] = objs_data.pop(k, None)
                        elif k == "regularMarketPrice":
                            objs_data['close'] = Decimal(objs_data.pop(k))
                        elif k == "validRanges":
                            objs_data['ranges'] = str(objs_data.pop(k))
                        elif k == "historicalDataPrice":
                            for k_ in _[k]:
                                if k_['high'] and k_['low']:
                                    dt_h = datetime.fromtimestamp(k_['date'])
                                    if dt_h > datetime.strptime(str(datetime.now().date()), "%Y-%m-%d"):

                                        objs_data['max'] = k_['high']
                                        objs_data['min'] = k_['low']
                                        objs_data['media'] = (
                                            k_['high'] + k_['low']) / 2
                                    br_zone = pytz.timezone('America/Sao_Paulo')
                                    dt_h = br_zone.localize(dt_h)
                                    k_.pop('date')
                                    k_.pop('volume')
                                    k_.pop('open')
                                    tk = Ticker.objects.get(ticker=ticker)
                                    if not HistoricTicker.objects.filter(ticker=tk, dt=dt_h).exists():
                                        HistoricTicker.objects.update_or_create(
                                            ticker=tk,
                                            dt=dt_h,
                                            defaults=k_

                                        )
                        else:
                            objs_data.pop(k)

                    if ticker:
                        Ticker.objects.update_or_create(
                            ticker=ticker,
                            defaults=objs_data
                        )
