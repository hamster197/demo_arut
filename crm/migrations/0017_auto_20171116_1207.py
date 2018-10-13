# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-16 09:07
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0016_auto_20171006_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='flat_obj_gal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True, verbose_name='Дата создания')),
                ('npict', models.ImageField(upload_to='image/%Y/%m/%d', verbose_name='Фото объекта')),
            ],
            options={
                'verbose_name_plural': 'Квартиры галерея',
                'verbose_name': 'Квартиры галерея',
            },
        ),
        migrations.AddField(
            model_name='flat_obj',
            name='domclick',
            field=models.CharField(choices=[('Да', 'Да'), ('Нет', 'Нет')], default='Нет', max_length=3, verbose_name='Домклик'),
        ),
        migrations.AddField(
            model_name='flat_obj',
            name='domclick_pub',
            field=models.CharField(choices=[('Да', 'Да'), ('Нет', 'Нет')], default='Нет', max_length=3, verbose_name='Опубликовать на Домклик'),
        ),
        migrations.AddField(
            model_name='flat_obj',
            name='etagnost',
            field=models.IntegerField(default='5', verbose_name='Этажность'),
        ),
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
        migrations.AddField(
            model_name='flat_obj_gal',
            name='id_gal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='idd_gal', to='crm.flat_obj', verbose_name='Название'),
        ),
    ]