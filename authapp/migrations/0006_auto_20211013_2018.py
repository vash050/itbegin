# Generated by Django 3.1.7 on 2021-10-13 20:18

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0005_auto_20211013_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactuser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 15, 20, 18, 21, 802210, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]