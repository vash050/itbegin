from django.contrib.auth.views import LoginView
from django.shortcuts import render

from authapp.forms import SiteUserLoginForm


class Login(LoginView):
    form = SiteUserLoginForm


# def Login(request):
#     form = SiteUserLoginForm
#     context = {
#         'form': form
#     }
#     return render(request, 'registration/login.html', context=context)
