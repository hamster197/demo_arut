# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-08 11:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0040_otchet_nov_rielt_proc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat_obj',
            name='dom_numb',
            field=models.CharField(default='', help_text='например: 36 или 11/2 или 16к (Буква обязательно маленкая!)', max_length=7, verbose_name='Номер дома:'),
        ),
    ]
