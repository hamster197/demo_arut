# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 08:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_auto_20171003_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed_gallery',
            name='pict',
            field=models.ImageField(upload_to='image/%Y/%m/%d', verbose_name='Картинка'),
        ),
    ]
