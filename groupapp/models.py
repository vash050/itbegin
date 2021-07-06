from django.apps import AppConfig
from django.db import models
from django.db.models.signals import post_save, m2m_changed
from django.dispatch.dispatcher import receiver

from django.urls import reverse

from authapp.models import SiteUser, Professions
from mainapp.models import Task


class Group(models.Model):
    name = models.CharField(max_length=120)
    author = models.ForeignKey(to=SiteUser, related_name='author_group', on_delete=models.CASCADE)
    description = models.CharField(max_length=200, blank=True)
    need_profession = models.ManyToManyField(to=Professions, through='DescriptionNeedProfessions')
    team_members = models.ManyToManyField(to=SiteUser, through='MemberTeam')
    logotype = models.ImageField(blank=True)
    got_task = models.ManyToManyField(to=Task, related_name='got_task', null=True)
    done_task = models.ManyToManyField(to=Task, related_name='done_task', blank=True)
    # groups_chat = models.URLField()
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('groupapp:group', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'команда'
        verbose_name_plural = 'команды'


class DescriptionNeedProfessions(models.Model):
    profession = models.ForeignKey(Professions, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    description = models.TextField(blank=True)


class ApplicationToNeedProfession(models.Model):
    to_need_profession = models.ForeignKey(DescriptionNeedProfessions, on_delete=models.CASCADE)
    author_application = models.ForeignKey(SiteUser, on_delete=models.CASCADE)
    date_create = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    acceptation = models.IntegerField(default=0)
    description_self = models.TextField(blank=True)


class MemberTeam(models.Model):
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    user_id = models.ForeignKey(SiteUser, on_delete=models.CASCADE)


