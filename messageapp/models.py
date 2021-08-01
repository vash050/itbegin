from django.db import models
from django.urls import reverse
from wagtail.core.fields import RichTextField

from authapp.models import SiteUser


class Dialog(models.Model):
    members = models.ManyToManyField(SiteUser, verbose_name='участник')

    def get_absolute_url(self):
        return reverse('messageapp:messages', kwargs={'dialog_id': self.pk})


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
