# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-09-27 13:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0117_auto_20180927_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat_obj',
            name='date_vigr_sait',
            field=models.DateField(blank=True, verbose_name='Дата выгрузки на сайт:'),
        ),
    ]
