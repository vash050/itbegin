# Generated by Django 3.1.7 on 2021-08-12 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forumapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='branch',
            options={'verbose_name': 'тема', 'verbose_name_plural': 'подтемы'},
        ),
        migrations.AlterModelOptions(
            name='forummessage',
            options={'verbose_name': 'сообщение', 'verbose_name_plural': 'собщения'},
        ),
        migrations.AlterModelOptions(
            name='maintopic',
            options={'verbose_name': 'раздел', 'verbose_name_plural': 'разделы'},
        ),
        migrations.AlterModelOptions(
            name='subtopic',
            options={'verbose_name': 'подраздел', 'verbose_name_plural': 'подразделы'},
        ),
        migrations.AlterField(
            model_name='branch',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forumapp.subtopic'),
        ),
    ]
