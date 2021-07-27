# Generated by Django 3.1.7 on 2021-07-27 10:41

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('avatar', models.ImageField(blank=True, upload_to='user_avatars', verbose_name='аватар пользователя')),
                ('date_born', models.DateField(null=True, verbose_name='день рождения')),
                ('about_me', models.CharField(blank=True, max_length=1000, verbose_name='обо мне')),
                ('link_to_portfolio', models.CharField(blank=True, max_length=150)),
                ('free', models.BooleanField(default=True)),
                ('date_update_profile', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'пользователь',
                'verbose_name_plural': 'пользователи',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Professions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession_name', models.CharField(max_length=120, verbose_name='профессия')),
            ],
            options={
                'verbose_name': 'профессии',
                'verbose_name_plural': 'профессии',
            },
        ),
        migrations.CreateModel(
            name='ContactUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_phone', models.CharField(blank=True, max_length=20, verbose_name='телефон')),
                ('user_email', models.EmailField(blank=True, max_length=254, verbose_name='email')),
                ('user_instagram', models.URLField(blank=True, verbose_name='инстаграмм')),
                ('user_vk', models.URLField(blank=True, verbose_name='вконтакте')),
                ('user_telegram', models.URLField(blank=True, verbose_name='телеграмм')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'контакты',
                'verbose_name_plural': 'контакты',
            },
        ),
        migrations.AddField(
            model_name='siteuser',
            name='profession',
            field=models.ManyToManyField(blank=True, to='authapp.Professions', verbose_name='профессии'),
        ),
        migrations.AddField(
            model_name='siteuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
