# Generated by Django 3.1.7 on 2021-04-10 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20210406_1532'),
        ('groupapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='done_task',
            field=models.ManyToManyField(blank=True, related_name='done_task', to='mainapp.Task'),
        ),
    ]