# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-25 13:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zvonki', '0014_auto_20180725_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zvonok',
            name='prezvonit',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 7, 25, 16, 46, 18, 179344), verbose_name='Перезвонить: '),
        ),
    ]
