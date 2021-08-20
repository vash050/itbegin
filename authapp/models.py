from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class SiteUser(AbstractUser):
    avatar = models.ImageField(verbose_name="аватар пользователя", upload_to="user_avatars", blank=True)
    date_born = models.DateField(verbose_name="день рождения", null=True)
    profession = models.ManyToManyField(verbose_name="профессии", to='Professions', blank=True)
    about_me = models.CharField(verbose_name="обо мне", max_length=1000, blank=True)
    link_to_portfolio = models.CharField(max_length=150, blank=True)
    free = models.BooleanField(default=True)
    date_update_profile = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def avatar_or_default(self, default_path="../static/img/avatar.png"):
        if self.avatar:
            return self.avatar
        return default_path


class ContactUser(models.Model):
    user = models.OneToOneField(SiteUser, unique=True, null=False, db_index=True, on_delete=models.CASCADE)
    user_phone = models.CharField(verbose_name="телефон", max_length=20, blank=True)
    user_email = models.EmailField(verbose_name="email", blank=True)
    user_instagram = models.URLField(verbose_name="инстаграмм", blank=True)
    user_vk = models.URLField(verbose_name="вконтакте", blank=True)
    user_telegram = models.URLField(verbose_name="телеграмм", blank=True)

    class Meta:
        verbose_name = 'контакты'
        verbose_name_plural = 'контакты'

    def get_absolute_url(self):
        return reverse('authapp:profile')


class Professions(models.Model):
    profession_name = models.CharField(verbose_name="профессия", max_length=120)

    class Meta:
        verbose_name = 'профессии'
        verbose_name_plural = 'профессии'

    def __str__(self):
        return self.profession_name
