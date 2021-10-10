import logging

from django.conf import settings
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.contrib.auth.views import PasswordChangeView
from django.core.mail import send_mail
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import UpdateView, DetailView, ListView

from authapp.forms import SiteUserLoginForm, SiteUserRegisterForm, SiteUserUpdateForm, SiteUserUpdateContact
from authapp.models import SiteUser, ContactUser

import logs.log_conf

SERVER_LOGGER = logging.getLogger('server')


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

    content = {"title": title, "forms": login_form}
    return render(request, "authapp/login.html", content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("mainapp:index"))


def profile(request):
    title = 'личный кабинет'
    user = SiteUser.objects.get(id=request.user.id)
    professions = user.profession.all()
    contact = ContactUser.objects.get(user_id=request.user.id)
    unread_dialogs_counter = user.dialog_set.unread(user=request.user).count()
    content = {
        'title': title,
        'professions': professions,
        'contact': contact,
        'unread_dialogs_counter': unread_dialogs_counter,
    }

    return render(request, 'authapp/profile.html', context=content)


def register(request):
    title = "регистрация"

    if request.method == "POST":
        register_form = SiteUserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            user = register_form.save()
            if send_verify_mail(user):
                SERVER_LOGGER.info(f"сообщение для потверждения регистрации отправлено")
                return HttpResponseRedirect(reverse("authapp:login"))
            SERVER_LOGGER.critical(f"ошибка отправки сообщения для потверждения регистрации")
            return HttpResponseRedirect(reverse('authapp:login'))
    else:
        register_form = SiteUserRegisterForm()

    content = {
        "title": title,
        "forms": register_form
    }
    return render(request, "authapp/register.html", content)


def update(request):
    title = "изменения профиля"

    if request.method == "POST":
        form = SiteUserUpdateForm(request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('authapp:profile'))
    else:
        form = SiteUserUpdateForm(instance=request.user)

    content = {
        "title": title,
        "forms": form
    }
    return render(request, "authapp/chang_profile.html", content)


class UserProfile(DetailView):
    model = get_user_model()


class UserSetting(ListView):
    """
    settings profile
    """
    model = get_user_model()


class UpdateUserContact(UpdateView):
    model = ContactUser
    form_class = SiteUserUpdateContact


class ChangePassword(PasswordChangeView):
    model = SiteUser
    template_name = 'authapp/change_password_form.html'


def send_verify_mail(user):
    verify_link = reverse("authapp:verify", args=[user.email, user.activation_key])

    tittle = f"подтверждение учетной записи {user.username}"
    message = f"Для потверждения учетной записи {user.username} на портале {settings.DOMAIN_NAME} прейти по ссылке: \
        \n{settings.DOMAIN_NAME}{verify_link}"

    SERVER_LOGGER.debug(f"from: {settings.EMAIL_HOST_USER}, to: {user.email}")
    return send_mail(tittle, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False, )


def verify(request, email, activation_key):
    try:
        user = SiteUser.objects.get(email=email)
        if user.activation_key == activation_key and not user.is_activation_key_expired():
            SERVER_LOGGER.debug(f"user {user} is activated")
            user.is_active = True
            user.save()
            auth.login(request, user)

            return render(request, "authapp/verification.html")

        SERVER_LOGGER.critical(f"error activation user: {user}")
        return render(request, "authapp/verification.html")
    except Exception as e:
        SERVER_LOGGER.critical(f"error activation user: {e.args}")

    return HttpResponseRedirect(reverse("mainapp:index"))
