from django.contrib import auth
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.forms import SiteUserLoginForm, SiteUserRegisterForm
from authapp.models import Professions, SiteUser


def login(request):
    title = "вход"

    login_form = SiteUserLoginForm(data=request.POST or None)

    if request.method == "POST" and login_form.is_valid():
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse("mainapp:index"))

    content = {"title": title, "login_form": login_form}
    return render(request, "authapp/login.html", content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("mainapp:index"))


def profile(request):
    title = 'личный кабинет'
    content = {"title": title}
    return render(request, 'authapp/profile.html', context=content)


def register(request):
    title = "регистрация"

    if request.method == "POST":
        register_form = SiteUserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('mainapp:index'))
    else:
        register_form = SiteUserRegisterForm()

    content = {
        "title": title,
        "register_form": register_form
    }
    return render(request, "authapp/register.html", content)
