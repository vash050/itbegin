# Generated by Django 3.1.7 on 2021-10-13 19:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_auto_20211013_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 15, 19, 4, 20, 67806, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]