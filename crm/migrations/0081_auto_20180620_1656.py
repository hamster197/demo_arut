# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-20 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0080_auto_20180620_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile1',
            name='search_maxc',
            field=models.IntegerField(default=100000000, verbose_name='Макс.цена'),
        ),
        migrations.AddField(
            model_name='userprofile1',
            name='search_maxp',
            field=models.IntegerField(default=5000, verbose_name='Макс.площадь'),
        ),
        migrations.AddField(
            model_name='userprofile1',
            name='search_minc',
            field=models.IntegerField(default=0, verbose_name='Мин.цена'),
        ),
        migrations.AddField(
            model_name='userprofile1',
            name='search_minp',
            field=models.IntegerField(default=0, verbose_name='Мин.площадь'),
        ),
        migrations.AddField(
            model_name='userprofile1',
            name='search_raion',
            field=models.CharField(choices=[('Любой', 'Любой'), ('Ахун', 'Ахун'), ('Бытха', 'Бытха'), ('Виноградная', 'Виноградная'), ('Дагомыс', 'Дагомыс'), ('Донская', 'Донская'), ('Донская(Пасечная)', 'Донская(Пасечная)'), ('Донская(Тимерязева)', 'Донская(Тимерязева)'), ('Завокзальный', 'Завокзальный'), ('Заречный', 'Заречный'), ('Клубничная', 'Клубничная'), ('КСМ', 'КСМ'), ('Красная поляна', 'Красная поляна'), ('Кудепста', 'Кудепста'), ('Макаренко', 'Макаренко'), ('Мамайка', 'Мамайка'), ('Мамайский перевал', 'Мамайский перевал'), ('Мацеста', 'Мацеста'), ('Н.Сочи', 'Н.Сочи'), ('Объезная', 'Объезная'), ('Пластунская', 'Пластунская'), ('Приморье', 'Приморье'), ('Раздольное', 'Раздольное'), ('Светлана', 'Светлана'), ('Соболевка', 'Соболевка'), ('Транспортная', 'Транспортная'), ('Фабрициуса', 'Фабрициуса'), ('Хоста', 'Хоста'), ('Центр', 'Центр'), ('(А) Блиново(+Вес)', '(А) Блиново(+Вес)'), ('(А) Гол. дали', '(А) Гол. дали'), ('(А) Кур.гор(+Чкал)', '(А) Кур.гор(+Чкал)'), ('(А) Мирный', '(А) Мирный'), ('(А) Молдовка', '(А) Молдовка'), ('(А) Центр', '(А) Центр'), ('(А) Чай совхоз', '(А) Чай совхоз')], default='Любой', max_length=25, verbose_name='Район'),
        ),
    ]
