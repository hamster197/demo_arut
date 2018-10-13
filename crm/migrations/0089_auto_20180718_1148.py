# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-18 08:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0088_auto_20180717_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zayavka',
            name='kanal',
            field=models.CharField(choices=[('Заявка с сайта', 'Заявка с сайта'), ('Заявка с сайта новостройка', 'Заявка с сайта новостройка'), ('Заявка с Avito', 'Заявка с Avito'), ('Тел. звонок', 'Тел. звонок'), ('Домклик', 'Домклик'), ('Личный', 'Личный')], default='Тел. звонок', max_length=35, verbose_name='Канал привлечения'),
        ),
    ]
