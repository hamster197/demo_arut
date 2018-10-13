# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-19 09:51
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0016_auto_20171006_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='etag',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30')], max_length=3, verbose_name='Этаж:'),
        ),
        migrations.AlterField(
            model_name='feed',
            name='etagnost',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30')], max_length=3, verbose_name='Этажность'),
        ),
        migrations.AlterField(
            model_name='feed',
            name='plosgad',
            field=models.IntegerField(help_text='min 10', validators=[django.core.validators.MinValueValidator(10)], verbose_name='Общая площадь:'),
        ),
        migrations.AlterField(
            model_name='feed',
            name='prais',
            field=models.IntegerField(help_text='min 500 000', validators=[django.core.validators.MinValueValidator(500000)], verbose_name='Цена:'),
        ),
    ]
