# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-24 08:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zvonki', '0006_auto_20180720_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zvonok',
            name='prim',
            field=models.TextField(blank=True, verbose_name='Первичная информация:'),
        ),
        migrations.AlterField(
            model_name='zvonok',
            name='status_zvonka',
            field=models.CharField(choices=[('Перезвонить', 'Перезвонить'), ('Недозвонился', 'Недозвонился'), ('В работе', 'В работе'), ('Архив', 'Архив'), ('В общем доступе', 'В общем доступе')], default='Перезвонить', max_length=55, verbose_name='Статус звонка'),
        ),
    ]
