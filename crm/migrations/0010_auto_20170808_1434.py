# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-08 11:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crm', '0009_auto_20170808_1320'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='uchastok',
            options={'verbose_name': 'Участки', 'verbose_name_plural': 'Участки'},
        ),
        migrations.AddField(
            model_name='uchastok',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='doma',
            name='gaz',
            field=models.CharField(choices=[('Нет', 'Нет'), ('Есть', 'Есть'), ('Можно подключить', 'Можно подключить'), ('В процессе подключения', 'В процессе подключения')], max_length=45, verbose_name='Газ'),
        ),
        migrations.AlterField(
            model_name='uchastok',
            name='comunications',
            field=models.CharField(choices=[('На участке', 'На участвке'), ('На границе', 'На границе'), ('Нет', 'Нет')], max_length=25, verbose_name='Комуникации'),
        ),
    ]
