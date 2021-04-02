from django.contrib.auth.models import AbstractUser
from django.db import models


class SiteUser(AbstractUser):
    avatar = models.ImageField(upload_to="user_avatars", blank=True)
    surname = models.CharField(max_length=150, blank=True)
    date_born = models.DateField(null=True)
    # profession = models.ManyToManyField(to='Professions', blank=True)
    about_me = models.CharField(max_length=1000, blank=True)
    link_to_portfolio = models.CharField(max_length=150, blank=True)
    # my_groups = models.ManyToManyField(to='Groups', blank=True)
    # my_projects = models.ManyToManyField(to='Projects', blank=True)
    free = models.BooleanField(default=True)
    date_last_login = models.DateTimeField(null=True)
    date_updata_profile = models.DateTimeField(auto_now=True)


class ContactUser(models.Model):
    user = models.OneToOneField(SiteUser, unique=True, null=False, db_index=True, on_delete=models.CASCADE)
    user_phone = models.CharField(max_length=20)
    user_email = models.EmailField(blank=True)
    user_instagram = models.URLField(blank=True)
    user_vk = models.URLField(blank=True)
    user_telegram = models.URLField(blank=True)
