from django.db import models
from django.urls import reverse
from wagtail.core.fields import RichTextField

from authapp.models import SiteUser


class ChatManager(models.Manager):
    use_for_related_fields = True

    # Метод принимает пользователя, для которого должна производиться выборка
    # Если пользователь не добавлен, то будет возвращены все диалоги,
    # в которых хотя бы одно сообщение не прочитано
    def unread(self, user=None):
        qs = self.get_queryset().exclude(last_message__isnull=True).filter(last_message__is_read=False)
        return qs.exclude(last_message__author=user) if user else qs


class Dialog(models.Model):
    members = models.ManyToManyField(SiteUser, verbose_name='участник')
    last_message = models.ForeignKey('Message', related_name='last_message', null=True, on_delete=models.SET_NULL)
    objects = ChatManager()

    def get_absolute_url(self):
        return reverse('messageapp:dialog', kwargs={'dialog_id': self.pk})


class Message(models.Model):
    dialog = models.ForeignKey(Dialog, verbose_name='чат', on_delete=models.CASCADE)
    author = models.ForeignKey(SiteUser, verbose_name='отправитель', on_delete=models.CASCADE)
    # message = RichTextField(verbose_name='сообщения', blank=True)
    message = models.TextField(verbose_name='сообщения', blank=True)
    pub_date = models.DateTimeField(verbose_name='дата сообщения', auto_now_add=True)
    is_read = models.BooleanField(verbose_name='прочитано', default=False)
    is_active = models.BooleanField(verbose_name='удалено', default=True)

    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        return self.message

    def get_absolute_url(self):
        return reverse('messageapp:dialog', kwargs={'dialog': self.dialog})
