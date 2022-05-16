from django.urls import include, path


from . import views as ticker_views

urlpatterns = [
    path('ticker-create/',
         ticker_views.user_vs_ticker_create, name='ticker_create'),

    path('ticker-update/',
         ticker_views.user_vs_ticker_update, name='ticker_update'),

    path('ticker-delete/',
         ticker_views.user_vs_ticker_delete, name='ticker_delete'),

    path('ticker-search/', ticker_views.ticker_search, name='ticker_search'),

    path('ticker-data/<str:ticker_pk>',
         ticker_views.ticker_data, name='ticker_data'),

]
