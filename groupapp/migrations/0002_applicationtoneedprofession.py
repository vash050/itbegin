# Generated by Django 3.1.7 on 2021-06-20 17:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groupapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationToNeedProfession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('acceptation', models.IntegerField(default=0)),
                ('description_self', models.TextField(blank=True)),
                ('author_application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('to_need_profession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groupapp.descriptionneedprofessions')),
            ],
        ),
    ]