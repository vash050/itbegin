from django.db import models

from authapp.models import SiteUser, Professions


class CategoryTask(models.Model):
    name = models.CharField(verbose_name='название', max_length=150)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(verbose_name='название', max_length=150)
    short_description = models.CharField(verbose_name='краткое описанние', max_length=1000)
    full_description = models.TextField(verbose_name='полное описание')
    tz = models.TextField(verbose_name='техническое задание')
    author = models.ForeignKey(to=SiteUser, on_delete=models.CASCADE)
    # developers = models.ManyToManyField(to=Groups)
    category = models.ForeignKey(CategoryTask, on_delete=models.CASCADE)
    professions = models.ManyToManyField(to=Professions)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    quantity_take = models.IntegerField(verbose_name='количество взятий', default=0)
    quantity_finished = models.IntegerField(verbose_name='количество выполнения', default=0)
    # reviews = models.ManyToManyField()
    rating = models.SmallIntegerField(default=0)

    class Meta:
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'

    def __str__(self):
        return self.name
