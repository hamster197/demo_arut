# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 13:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clients',
            name='otd',
        ),
        migrations.AlterField(
            model_name='feed',
            name='nazv',
            field=models.CharField(default='', max_length=100, verbose_name='Название:'),
        ),
    ]
