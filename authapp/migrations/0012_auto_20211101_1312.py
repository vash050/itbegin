# Generated by Django 3.1.7 on 2021-11-01 13:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0011_auto_20211101_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 3, 13, 12, 27, 526973, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
