# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-05 14:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0026_auto_20180105_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat_obj',
            name='domclick',
            field=models.CharField(choices=[('Да', 'Да'), ('Нет', 'Нет')], default='Нет', max_length=3, verbose_name='Yandex'),
        ),
        migrations.AddField(
            model_name='userprofile1',
            name='ya',
            field=models.CharField(choices=[('Да', 'Да'), ('Нет', 'Нет')], default='Нет', max_length=3, verbose_name='Yandex недвижимость'),
        ),
    ]