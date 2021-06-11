from django.db import models

from authapp.models import SiteUser, Professions
from mainapp.models import Task


class Group(models.Model):
    name = models.CharField(max_length=120)
    # При удаление бд убрать null=True
    author = models.ForeignKey(to=SiteUser,related_name='author_group', on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=200, blank=True)
    need_profession = models.ManyToManyField(to=Professions, through='DescriptionNeedProfessions')
    team_members = models.ManyToManyField(to=SiteUser, null=True)
    logotype = models.ImageField(blank=True)
    got_task = models.ManyToManyField(to=Task, related_name='got_task', null=True)
    done_task = models.ManyToManyField(to=Task, related_name='done_task', blank=True)
    # groups_chat = models.URLField()
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'команда'
        verbose_name_plural = 'команды'


class DescriptionNeedProfessions(models.Model):
    profession = models.ForeignKey(Professions, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    description = models.TextField(blank=True)

