# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-20 10:47
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zvonki', '0002_auto_20180720_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='zvonok',
            name='cena',
            field=models.IntegerField(blank=True, default=800000, validators=[django.core.validators.MinValueValidator(300000)], verbose_name='Бюджет до:'),
        ),
        migrations.AddField(
            model_name='zvonok',
            name='raion',
            field=models.CharField(choices=[('Выбор района', 'Выбор района'), ('Ахун', 'Ахун'), ('Бытха', 'Бытха'), ('Виноградная', 'Виноградная'), ('Дагомыс', 'Дагомыс'), ('Донская', 'Донская'), ('Донская(Пасечная)', 'Донская(Пасечная)'), ('Донская(Тимерязева)', 'Донская(Тимерязева)'), ('Завокзальный', 'Завокзальный'), ('Заречный', 'Заречный'), ('Клубничная', 'Клубничная'), ('КСМ', 'КСМ'), ('Красная поляна', 'Красная поляна'), ('Кудепста', 'Кудепста'), ('Макаренко', 'Макаренко'), ('Мамайка', 'Мамайка'), ('Мамайский перевал', 'Мамайский перевал'), ('Мацеста', 'Мацеста'), ('Н.Сочи', 'Н.Сочи'), ('Объезная', 'Объезная'), ('Пластунская', 'Пластунская'), ('Приморье', 'Приморье'), ('Раздольное', 'Раздольное'), ('Светлана', 'Светлана'), ('Соболевка', 'Соболевка'), ('Транспортная', 'Транспортная'), ('Фабрициуса', 'Фабрициуса'), ('Хоста', 'Хоста'), ('Центр', 'Центр'), ('(А) Блиново(+Вес)', '(А) Блиново(+Вес)'), ('(А) Гол. дали', '(А) Гол. дали'), ('(А) Кур.гор(+Чкал)', '(А) Кур.гор(+Чкал)'), ('(А) Мирный', '(А) Мирный'), ('(А) Молдовка', '(А) Молдовка'), ('(А) Центр', '(А) Центр'), ('(А) Чай совхоз', '(А) Чай совхоз')], default='Неважно', max_length=20, verbose_name='Район'),
        ),
        migrations.AddField(
            model_name='zvonok',
            name='status_zvonka',
            field=models.CharField(default='Перезвонить', max_length=55, verbose_name='Статус звонка'),
        ),
        migrations.AddField(
            model_name='zvonok',
            name='subj',
            field=models.CharField(choices=[('Неважно', 'Неважно'), ('Студия', 'Студия'), ('Однокомнатная', 'Однокомнатная'), ('Двухкомнатная', 'Двухкомнатная'), ('Многокомнатная', 'Многокомнатная'), ('Дом', 'Дом'), ('Участок', 'Участок'), ('Коммерция', 'Коммерция')], default='Неважно', max_length=50, verbose_name='Что ищет:'),
        ),
    ]
