# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-31 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zvonki', '0020_auto_20180731_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zvonok',
            name='prezvonit',
            field=models.DateTimeField(blank=True, verbose_name='Перезвонить: '),
        ),
    ]
