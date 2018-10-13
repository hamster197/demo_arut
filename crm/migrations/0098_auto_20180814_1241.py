# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-08-14 09:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0097_auto_20180814_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat_obj',
            name='raion',
            field=models.CharField(choices=[('Выбор района', 'Выбор района'), ('Ахун', 'Ахун'), ('Барановка село', 'Барановка село'), ('Бытха', 'Бытха'), ('Виноградная', 'Виноградная'), ('Дагомыс', 'Дагомыс'), ('Донская', 'Донская'), ('Донская(Пасечная)', 'Донская(Пасечная)'), ('Донская(Тимерязева)', 'Донская(Тимерязева)'), ('Завокзальный', 'Завокзальный'), ('Заречный', 'Заречный'), ('Клубничная', 'Клубничная'), ('КСМ', 'КСМ'), ('Красная поляна', 'Красная поляна'), ('Кудепста', 'Кудепста'), ('Макаренко', 'Макаренко'), ('Мамайка', 'Мамайка'), ('Мамайский перевал', 'Мамайский перевал'), ('Мацеста', 'Мацеста'), ('Н.Сочи', 'Н.Сочи'), ('Объезная', 'Объезная'), ('Пластунская', 'Пластунская'), ('Приморье', 'Приморье'), ('Раздольное', 'Раздольное'), ('Светлана', 'Светлана'), ('Соболевка', 'Соболевка'), ('Транспортная', 'Транспортная'), ('Фабрициуса', 'Фабрициуса'), ('Хоста', 'Хоста'), ('Центр', 'Центр'), ('(А) Блиново(+Вес)', '(А) Блиново(+Вес)'), ('(А) Гол. дали', '(А) Гол. дали'), ('(А) Кур.гор(+Чкал)', '(А) Кур.гор(+Чкал)'), ('(А) Мирный', '(А) Мирный'), ('(А) Веселое', '(А) Веселое'), ('(А) Молдовка', '(А) Молдовка'), ('(А) Центр', '(А) Центр'), ('(А) Чай совхоз', '(А) Чай совхоз')], default='Адрес', max_length=20, verbose_name='Район'),
        ),
    ]
