from django.db import models

from authapp.models import SiteUser
from groupapp.models import Group


class RoomChat(models.Model):
    """
    room chat
    """
    group = models.OneToOneField(to=Group, on_delete=models.CASCADE)
    members = models.ManyToManyField(to=SiteUser, null=True)


class MessageChat(models.Model):
    """
    message chat
    """
    group = models.ForeignKey(to=RoomChat, on_delete=models.CASCADE)
    author = models.ForeignKey(to=SiteUser, on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
