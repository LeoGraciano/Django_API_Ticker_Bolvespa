from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from .forms import UserRegisterForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm


class Login(LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('index')


class Logout(LoginRequiredMixin, LogoutView):
    login_url = '/login/'
    next_page = reverse_lazy('login')


class RegisterCreateView(SuccessMessageMixin, CreateView):
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')
    form_class = UserRegisterForm
    success_message = "Sua conta foi Criada com Sucesso"
