# Generated by Django 3.1.7 on 2021-10-13 20:23

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0007_auto_20211013_2020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactuser',
            name='id',
        ),
        migrations.AlterField(
            model_name='contactuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 15, 20, 23, 44, 841651, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]