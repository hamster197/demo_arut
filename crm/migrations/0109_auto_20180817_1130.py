# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-08-17 08:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0108_auto_20180817_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zayavka',
            name='prim',
            field=models.CharField(max_length=850, verbose_name='Примечание:'),
        ),
    ]
