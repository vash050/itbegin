# Generated by Django 3.1.7 on 2021-08-19 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('messageapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dialog',
            name='last_message',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_message', to='messageapp.message'),
        ),
    ]