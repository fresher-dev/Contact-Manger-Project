from django.shortcuts import render
from .forms import RegisterForm
from django.views.generic import CreateView, TemplateView
import django.contrib.auth.views as auth_view


class Register(CreateView):
    form_class = RegisterForm
    template_name = "account/register.html"


class Login(auth_view.LoginView):
    template_name = "account/login.html"


class Logout(auth_view.LogoutView):
    pass
