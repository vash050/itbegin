from django.db import models
from django.urls import reverse
from django.utils import timezone

from authapp.models import SiteUser


class Chat(models.Model):
    DIALOG = 'D'
    CHAT = 'C'
    CHAT_TYPE_CHOICES = (
        (DIALOG, 'Dialog'),
        (CHAT, 'Chat')
    )

    type = models.CharField(verbose_name='Тип', max_length=1, choices=CHAT_TYPE_CHOICES, default=DIALOG)
    members = models.ManyToManyField(SiteUser, verbose_name='участник')

    def get_absolute_url(self):
        return reverse('messegeapp:messages', (), {'chat_id': self.pk})


class Message(models.Model):
    chat = models.ForeignKey(Chat, verbose_name='чат', on_delete=models.CASCADE)
    author = models.ForeignKey(SiteUser, verbose_name='пользователь', on_delete=models.CASCADE)
    massage = models.TextField(verbose_name='сообщения')
    pub_date = models.DateTimeField(verbose_name='дата сообщения', auto_now_add=True)
    is_read = models.BooleanField(verbose_name='прочитано', default=False)
    is_active = models.BooleanField(verbose_name='удалено', default=True)

    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        return self.massage
