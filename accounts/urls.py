from django.urls import path

from . import views as accounts_views

urlpatterns = [
    path('sign-up/', accounts_views.RegisterCreateView.as_view(), name='signup'),
    path('login/', accounts_views.Login.as_view(), name='login'),
    path('logout/', accounts_views.Logout.as_view(), name='logout')
]
