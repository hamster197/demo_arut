# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-30 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zvonki', '0016_auto_20180730_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zvonok',
            name='prezvonit',
            field=models.DateField(blank=True, verbose_name='Перезвонить: '),
        ),
    ]