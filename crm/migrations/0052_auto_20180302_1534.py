# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-02 12:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0051_auto_20180302_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='balcons',
            field=models.CharField(choices=[('Да', 'Да'), ('Нет', 'Нет')], default='Нет', max_length=3, verbose_name='Балкон'),
        ),
        migrations.AddField(
            model_name='feed',
            name='lift',
            field=models.CharField(choices=[('Да', 'Да'), ('Нет', 'Нет')], default='Нет', max_length=3, verbose_name='Лифт'),
        ),
    ]
