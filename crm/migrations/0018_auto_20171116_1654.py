# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-16 13:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0017_auto_20171116_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='SaleType',
            field=models.CharField(choices=[('dupt', 'Договор уступки права требования'), ('dzhsk', 'Договор ЖСК'), ('free', 'Свободная продажа'), ('fz214', '214-ФЗ'), ('investment', 'Договор инвестирования'), ('pdkp', 'Предварительный договор купли-продажи')], default='dupt', max_length=30, verbose_name='Тип продажи:'),
        ),
        migrations.AddField(
            model_name='feed',
            name='category',
            field=models.CharField(choices=[('flatSale', 'Вторичка'), ('newBuildingFlatSale', 'Квартира в новостройке')], default='flatSale', max_length=25, verbose_name='Тип недвижимости'),
        ),
        migrations.AlterField(
            model_name='flat_obj',
            name='etagnost',
            field=models.IntegerField(verbose_name='Этажность'),
        ),
    ]
