# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-26 10:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0061_auto_20180326_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat_obj',
            name='dom_numb',
            field=models.CharField(default='', help_text='например: 36 или 11/2 или 16к (Буква обязательно маленкая!)', max_length=37, verbose_name='Номер дома:'),
        ),
    ]
