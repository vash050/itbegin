# Generated by Django 3.1.7 on 2021-06-20 17:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='название')),
                ('short_description', models.CharField(max_length=1000, verbose_name='краткое описанние')),
                ('full_description', models.TextField(verbose_name='полное описание')),
                ('tz', models.TextField(verbose_name='техническое задание')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('quantity_take', models.IntegerField(default=0, verbose_name='количество взятий')),
                ('quantity_finished', models.IntegerField(default=0, verbose_name='количество выполнения')),
                ('rating', models.SmallIntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('professions', models.ManyToManyField(to='authapp.Professions')),
            ],
            options={
                'verbose_name': 'задача',
                'verbose_name_plural': 'задачи',
            },
        ),
    ]
