from django.db import models

from authapp.models import SiteUser


class MainTopic(models.Model):
    """
    глобальная тема
    """
    name = models.CharField(max_length=240)
    description = models.TextField()

    class Meta:
        verbose_name = 'раздел'
        verbose_name_plural = 'разделы'

    def __str__(self):
        return self.name


class SubTopic(models.Model):
    """
    подтема
    """
    name = models.CharField(max_length=240)
    description = models.TextField(blank=True)
    topic = models.ForeignKey(to=MainTopic, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'подраздел'
        verbose_name_plural = 'подразделы'

    def __str__(self):
        return self.name


class Branch(models.Model):
    """
    модель отдельной темы на форуме
    """
    name = models.CharField(max_length=240)
    description = models.TextField(blank=True)
    topic = models.ForeignKey(to=SubTopic, on_delete=models.CASCADE)
    author_branch_forum = models.ForeignKey(to=SiteUser, on_delete=models.PROTECT)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'тема'
        verbose_name_plural = 'подтемы'

    def __str__(self):
        return self.name


class ForumMessage(models.Model):
    """
    forum message
    """
    body = models.TextField()
    topic = models.ForeignKey(to=Branch, on_delete=models.CASCADE)
    author_branch_forum = models.ForeignKey(to=SiteUser, on_delete=models.PROTECT)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'собщения'
