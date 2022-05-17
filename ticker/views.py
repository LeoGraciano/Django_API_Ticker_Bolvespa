import json
from django.core.serializers.json import DjangoJSONEncoder
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.template.loader import render_to_string
from core.models import UserVsTicker
from core.forms import UserVsTickerForm
from .models import HistoricTicker, Ticker
from django.db.models import F, Q, Max, Value

User = get_user_model()

# Create your views here.


def save_ticker_form(request, template_name, form):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()

            data['form_is_valid'] = True
            messages.success(
                request, f'Card: Salvo com Sucesso')
        else:
            data['form_is_valid'] = False
            messages.error(request, 'Falha ao Salvar Dados')

        return redirect('index')
    context = {
        'form': form,
    }
    data['html_form'] = render_to_string(
        template_name, context, request=request)
    return JsonResponse(data)


@ login_required(login_url='login/')
def user_vs_ticker_create(request):
    if request.method == 'POST':
        form = UserVsTickerForm(request.POST, request.FILES)
    else:
        form = UserVsTickerForm()

    return save_ticker_form(request, 'ticker/uvt-create.html', form)


@ login_required(login_url='login/')
def user_vs_ticker_update(request):
    UserVsTicker.objects.get_or_create(user=request.user)[0]
    if request.method == 'POST':
        form = UserVsTickerForm(request.POST)
        if form.is_valid():
            form.save()
            tk = form.cleaned_data.get('ticker').ticker
            messages.success(
                request, f'Ticker {tk}: salvo com Sucesso')

        else:
            if form.errors:
                for k, v in form.errors.items():
                    messages.error(request, v)
            else:
                messages.error(request, 'Falha ao Salvar Dados')

        return redirect('index')
    else:
        form = UserVsTickerForm()

    return save_ticker_form(request, 'ticker/uvt-update.html', form)


@ login_required(login_url='/login/')
def user_vs_ticker_delete(request):

    if request.method == 'POST':
        ticker = request.POST.get('ticker', None)
        if ticker:
            obj = Ticker.objects.get(ticker=ticker)
            UserVsTicker.objects.get(user=request.user).ticker.remove(obj)
            messages.success(
                request, f'Card: {obj.ticker}, deletado com sucesso')
        else:
            messages.error(
                request, f'{ticker}, não existe')

    return redirect('index')


@ login_required(login_url='/login/')
def ticker_search(request):

    response = {}

    search = (request.GET.get('s')).upper()
    option = (request.GET.get('option'))

    qs_ticker = Ticker.objects.filter(
        ticker__icontains=search)

    qs_name = Ticker.objects.filter(
        name__icontains=search)

    qs_total = (qs_ticker | qs_name).distinct()

    if option == 'add':
        uvt = UserVsTicker.objects.get_or_create(user=request.user)[0]
        fill = ''
        if uvt:
            fill = uvt.ticker.all().values_list('ticker', flat=True)

        qs_total = qs_total.exclude(ticker__in=fill)

    elif option == 'del':
        uvt = UserVsTicker.objects.get_or_create(user=request.user)[0]
        if uvt:
            fill = uvt.ticker.all().values_list('ticker', flat=True)

        qs_total = qs_total.filter(ticker__in=fill)

    if qs_total.exists():
        qs_val = qs_total.values_list(
            'ticker')
        ticker_list = []
        for obj in qs_val:

            obj_str = f'{obj[0]}'
            obj_str = obj_str.strip()
            ticker_list.append(obj_str)

            response = {
                'status': 200,
                'result': ticker_list,
            }

            return JsonResponse(response)

    response = {
        'status': 400,
        'result': [],
    }

    return JsonResponse(response)


@ login_required(login_url='/login/')
def ticker_data(request, ticker_pk):
    tickers = HistoricTicker.objects.filter(
        ticker__pk=ticker_pk).order_by('dt')

    ticker_list = [model_to_dict(x) for x in tickers]

    term = {
        'result': ticker_list,
        'label': f"{tickers[0].ticker.ticker} - {tickers[0].ticker.name}"
    }

    data = term
    return JsonResponse(data)
