from django.contrib.auth.views import LoginView
from django.shortcuts import render

from authapp.forms import SiteUserLoginForm


class Login(LoginView):
    form = SiteUserLoginForm
    template_name = 'authapp/login.html'
