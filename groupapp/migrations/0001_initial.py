# Generated by Django 3.1.7 on 2021-07-06 13:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0001_initial'),
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DescriptionNeedProfessions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('logotype', models.ImageField(blank=True, upload_to='')),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_group', to=settings.AUTH_USER_MODEL)),
                ('done_task', models.ManyToManyField(blank=True, related_name='done_task', to='mainapp.Task')),
                ('got_task', models.ManyToManyField(null=True, related_name='got_task', to='mainapp.Task')),
                ('need_profession', models.ManyToManyField(through='groupapp.DescriptionNeedProfessions', to='authapp.Professions')),
            ],
            options={
                'verbose_name': 'команда',
                'verbose_name_plural': 'команды',
            },
        ),
        migrations.CreateModel(
            name='MemberTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groupapp.group')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='team_members',
            field=models.ManyToManyField(through='groupapp.MemberTeam', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='descriptionneedprofessions',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groupapp.group'),
        ),
        migrations.AddField(
            model_name='descriptionneedprofessions',
            name='profession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authapp.professions'),
        ),
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
