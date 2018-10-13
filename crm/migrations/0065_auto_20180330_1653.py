# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-30 13:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0064_auto_20180329_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat_obj',
            name='etag',
            field=models.IntegerField(default=0, verbose_name='Этаж'),
        ),
        migrations.AlterField(
            model_name='flat_obj',
            name='etagnost',
            field=models.IntegerField(default=0, verbose_name='Этажность'),
        ),
        migrations.AlterField(
            model_name='flat_obj',
            name='kvart_numb',
            field=models.CharField(blank=True, default='', help_text='например: 11', max_length=5, verbose_name='Номер квартиры:'),
        ),
    ]