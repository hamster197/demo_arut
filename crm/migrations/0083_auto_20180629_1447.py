# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-29 11:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0082_auto_20180622_1414'),
    ]

    operations = [
        migrations.CreateModel(
            name='TmpCianCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adler', models.IntegerField(verbose_name='Адлер')),
                ('sochi', models.IntegerField(verbose_name='Сочи')),
            ],
            options={
                'verbose_name': 'Циан',
                'verbose_name_plural': 'Циан',
            },
        ),
        migrations.AddField(
            model_name='otchet_nov',
            name='pr_prosmotra_golovin',
            field=models.CharField(default='', max_length=3, verbose_name='Признак просмотра Головиным'),
        ),
    ]
