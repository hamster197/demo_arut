# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-08-10 12:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0095_auto_20180810_1427'),
    ]

    operations = [
        migrations.CreateModel(
            name='vestum_poryadok_feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True, verbose_name='Дата изменения')),
                ('poryadok', models.CharField(choices=[('ПоВозрастанию', 'ПоВозрастанию'), ('ПоУбыванию', 'ПоУбыванию')], max_length=25, verbose_name='Порядок выдачи в фиде Vestum')),
            ],
            options={
                'verbose_name': 'Порядок выдачи обьявлений в Циан',
                'verbose_name_plural': 'Порядок выдачи обьявлений в Циан',
            },
        ),
    ]