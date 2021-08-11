from django.db import models

from authapp.models import SiteUser


class MainTopic(models.Model):
    """
    глобальная тема
    """
    name = models.CharField(max_length=240)
    description = models.TextField()


class SubTopic(models.Model):
    """
    подтема
    """
    name = models.CharField(max_length=240)
    description = models.TextField(blank=True)
    topic = models.ForeignKey(to=MainTopic, on_delete=models.CASCADE)


class Branch(models.Model):
    """
    модель отдельной темы на форуме
    """
    name = models.CharField(max_length=240)
    description = models.TextField(blank=True)
    topic = models.OneToOneField(to=SubTopic, on_delete=models.CASCADE)
    author_branch_forum = models.ForeignKey(to=SiteUser, on_delete=models.PROTECT)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)


class ForumMessage(models.Model):
    """
    forum message
    """
    body = models.TextField()
    topic = models.ForeignKey(to=Branch, on_delete=models.CASCADE)
    author_branch_forum = models.ForeignKey(to=SiteUser, on_delete=models.PROTECT)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
