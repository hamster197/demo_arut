# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-28 11:22
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0005_auto_20170728_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='clients',
            name='category',
            field=models.CharField(choices=[('Квартиры', 'Квартиры'), ('Дома', 'Дома'), ('Участки', 'Участки')], default='Квартиры', max_length=45, verbose_name='Что ищет'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='auth_old',
            field=models.CharField(default='none', max_length=85, verbose_name='Автор(Был раньше):'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='budg_do',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(300000)], verbose_name='Бюджет до:'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='budg_ot',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(300000)], verbose_name='Бюджет от:'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='raion',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Ахун', 'Ахун'), ('Бытха', 'Бытха'), ('Дагомыс', 'Дагомыс'), ('Донская', 'Донская'), ('Донская', 'Донская'), ('Завокзальный', 'Завокзальный'), ('Заречный', 'Заречный'), ('Клубничная', 'Клубничная'), ('Красная поляна', 'Красная поляна'), ('Кудепста', 'Кудепста'), ('Макаренко', 'Макаренко'), ('Мамайка', 'Мамайка'), ('Мамайский перевал', 'Мамайский перевал'), ('Мацеста', 'Мацеста'), ('Н.Сочи', 'Н.Сочи'), ('Объезная', 'Объезная'), ('Приморье', 'Приморье'), ('Раздольное', 'Раздольное'), ('Светлана', 'Светлана'), ('Транспортная', 'Транспортная'), ('Фабрициуса', 'Фабрициуса'), ('Хоста', 'Хоста'), ('Центр', 'Центр')], max_length=216, verbose_name='Район:'),
        ),
    ]
