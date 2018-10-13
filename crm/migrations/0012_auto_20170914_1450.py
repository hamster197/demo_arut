# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-14 11:50
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crm', '0011_doma_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='otchet_nov',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_sozd', models.DateField(auto_now=True, verbose_name='Дата сделки:')),
                ('nazv_nov', models.CharField(max_length=140, verbose_name='Название новостройки:')),
                ('fio_kl', models.CharField(max_length=50, verbose_name='ФИО клиента:')),
                ('tel_kl', phonenumber_field.modelfields.PhoneNumberField(max_length=128, verbose_name='тел.Клиента:')),
                ('rielt_proc', models.IntegerField(default=100, verbose_name='Проценты:')),
                ('ploshad', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Площадь:')),
                ('stoimost', models.IntegerField(validators=[django.core.validators.MinValueValidator(300000)], verbose_name='Цена:')),
                ('komisia', models.IntegerField(validators=[django.core.validators.MinValueValidator(30000)], verbose_name='Комисия:')),
                ('ipoteka', models.CharField(choices=[('Да', 'Да'), ('Нет', 'Нет')], default='Нет', max_length=3, verbose_name='Ипотека:')),
                ('rasrochka', models.CharField(choices=[('Да', 'Да'), ('Нет', 'Нет')], default='Нет', max_length=3, verbose_name='Расрочка:')),
                ('rielt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Риелтор:')),
            ],
            options={
                'verbose_name': 'Отчет по сделке(Нов.)',
                'verbose_name_plural': 'Отчеты по сделке(Нов.)',
            },
        ),
        migrations.CreateModel(
            name='otchet_nov_date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_sd', models.DateField(verbose_name='Дата:')),
                ('nazv_nov_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.otchet_nov')),
            ],
            options={
                'verbose_name': 'Спр. даты сделок',
                'verbose_name_plural': 'Спр. дат сделок',
            },
        ),
        migrations.CreateModel(
            name='otchet_nov_reeltsp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proc', models.IntegerField(verbose_name='Проценты')),
                ('reelt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Риелтор в сделке:')),
                ('sdelka_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.otchet_nov')),
            ],
            options={
                'verbose_name': 'Сп.риелтор в сделке',
                'verbose_name_plural': 'Сп.риелтор в сделке',
            },
        ),
        migrations.AddField(
            model_name='clients',
            name='adress',
            field=models.CharField(default='Адрес', max_length=70, verbose_name='Адрес:'),
        ),
        migrations.AddField(
            model_name='doma',
            name='adress',
            field=models.CharField(default='Адрес', max_length=70, verbose_name='Адрес:'),
        ),
        migrations.AddField(
            model_name='flat_obj',
            name='adress',
            field=models.CharField(default='Адрес', max_length=70, verbose_name='Адрес:'),
        ),
        migrations.AddField(
            model_name='uchastok',
            name='adress',
            field=models.CharField(default='Адрес', max_length=70, verbose_name='Адрес:'),
        ),
        migrations.AddField(
            model_name='uchastok',
            name='ploshad',
            field=models.IntegerField(default='10', verbose_name='Площадь(соток)'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='raion',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Ахун', 'Ахун'), ('Бытха', 'Бытха'), ('Дагомыс', 'Дагомыс'), ('Донская', 'Донская'), ('Донская', 'Донская'), ('Завокзальный', 'Завокзальный'), ('Заречный', 'Заречный'), ('Клубничная', 'Клубничная'), ('КСМ', 'КСМ'), ('Красная поляна', 'Красная поляна'), ('Кудепста', 'Кудепста'), ('Макаренко', 'Макаренко'), ('Мамайка', 'Мамайка'), ('Мамайский перевал', 'Мамайский перевал'), ('Мацеста', 'Мацеста'), ('Н.Сочи', 'Н.Сочи'), ('Объезная', 'Объезная'), ('Пластунская', 'Пластунская'), ('Приморье', 'Приморье'), ('Раздольное', 'Раздольное'), ('Светлана', 'Светлана'), ('Транспортная', 'Транспортная'), ('Тимерязева', 'Тимирязева'), ('Фабрициуса', 'Фабрициуса'), ('Хоста', 'Хоста'), ('Центр', 'Центр')], max_length=243, verbose_name='Район:'),
        ),
        migrations.AlterField(
            model_name='doma',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='doma',
            name='canalizacia',
            field=models.CharField(choices=[('ЛОС', 'ЛОС'), ('Септик', 'Септик'), ('Центральная', 'Центральная')], max_length=45, verbose_name='Канализация'),
        ),
        migrations.AlterField(
            model_name='doma',
            name='ploshad_doma',
            field=models.IntegerField(verbose_name='Площадь дома'),
        ),
        migrations.AlterField(
            model_name='doma',
            name='raion',
            field=models.CharField(choices=[('Ахун', 'Ахун'), ('Бытха', 'Бытха'), ('Дагомыс', 'Дагомыс'), ('Донская', 'Донская'), ('Донская', 'Донская'), ('Завокзальный', 'Завокзальный'), ('Заречный', 'Заречный'), ('Клубничная', 'Клубничная'), ('КСМ', 'КСМ'), ('Красная поляна', 'Красная поляна'), ('Кудепста', 'Кудепста'), ('Макаренко', 'Макаренко'), ('Мамайка', 'Мамайка'), ('Мамайский перевал', 'Мамайский перевал'), ('Мацеста', 'Мацеста'), ('Н.Сочи', 'Н.Сочи'), ('Объезная', 'Объезная'), ('Пластунская', 'Пластунская'), ('Приморье', 'Приморье'), ('Раздольное', 'Раздольное'), ('Светлана', 'Светлана'), ('Транспортная', 'Транспортная'), ('Тимерязева', 'Тимирязева'), ('Фабрициуса', 'Фабрициуса'), ('Хоста', 'Хоста'), ('Центр', 'Центр')], max_length=45, verbose_name='Район:'),
        ),
        migrations.AlterField(
            model_name='doma',
            name='remont',
            field=models.CharField(choices=[('Черновой', 'Черновой'), ('Чистовой', 'Чистовой'), ('Дизайнерский', 'Дизайнерский'), ('Жилой', 'Жилой'), ('Новый', 'Новый')], max_length=55, verbose_name='Ремонт'),
        ),
        migrations.AlterField(
            model_name='doma',
            name='status_obj',
            field=models.CharField(choices=[('Опубликован', 'Опубликован'), ('Не опубликован', 'Не опубликован')], max_length=45, verbose_name='Публикация обьекта'),
        ),
        migrations.AlterField(
            model_name='flat_obj',
            name='ploshad',
            field=models.IntegerField(default='10', verbose_name='Площадь'),
        ),
        migrations.AlterField(
            model_name='flat_obj',
            name='raion',
            field=models.CharField(choices=[('Ахун', 'Ахун'), ('Бытха', 'Бытха'), ('Дагомыс', 'Дагомыс'), ('Донская', 'Донская'), ('Донская', 'Донская'), ('Завокзальный', 'Завокзальный'), ('Заречный', 'Заречный'), ('Клубничная', 'Клубничная'), ('КСМ', 'КСМ'), ('Красная поляна', 'Красная поляна'), ('Кудепста', 'Кудепста'), ('Макаренко', 'Макаренко'), ('Мамайка', 'Мамайка'), ('Мамайский перевал', 'Мамайский перевал'), ('Мацеста', 'Мацеста'), ('Н.Сочи', 'Н.Сочи'), ('Объезная', 'Объезная'), ('Пластунская', 'Пластунская'), ('Приморье', 'Приморье'), ('Раздольное', 'Раздольное'), ('Светлана', 'Светлана'), ('Транспортная', 'Транспортная'), ('Тимерязева', 'Тимирязева'), ('Фабрициуса', 'Фабрициуса'), ('Хоста', 'Хоста'), ('Центр', 'Центр')], default='Адрес', max_length=20, verbose_name='Район'),
        ),
        migrations.AlterField(
            model_name='flat_obj',
            name='remont',
            field=models.CharField(choices=[('Черновой', 'Черновой'), ('Чистовой', 'Чистовой'), ('Дизайнерский', 'Дизайнерский'), ('Жилой', 'Жилой'), ('Новый', 'Новый')], max_length=25, verbose_name='Ремонт'),
        ),
        migrations.AlterField(
            model_name='uchastok',
            name='comunications',
            field=models.CharField(choices=[('На участке', 'На участке'), ('На границе', 'На границе'), ('Нет', 'Нет')], max_length=25, verbose_name='Комуникации'),
        ),
        migrations.AlterField(
            model_name='uchastok',
            name='gaz',
            field=models.CharField(choices=[('Нет', 'Нет'), ('Есть', 'Есть'), ('Можно подключить', 'Можно подключить'), ('В процессе подключения', 'В процессе подключения')], max_length=45, verbose_name='Газ'),
        ),
        migrations.AlterField(
            model_name='uchastok',
            name='raion',
            field=models.CharField(choices=[('Ахун', 'Ахун'), ('Бытха', 'Бытха'), ('Дагомыс', 'Дагомыс'), ('Донская', 'Донская'), ('Донская', 'Донская'), ('Завокзальный', 'Завокзальный'), ('Заречный', 'Заречный'), ('Клубничная', 'Клубничная'), ('КСМ', 'КСМ'), ('Красная поляна', 'Красная поляна'), ('Кудепста', 'Кудепста'), ('Макаренко', 'Макаренко'), ('Мамайка', 'Мамайка'), ('Мамайский перевал', 'Мамайский перевал'), ('Мацеста', 'Мацеста'), ('Н.Сочи', 'Н.Сочи'), ('Объезная', 'Объезная'), ('Пластунская', 'Пластунская'), ('Приморье', 'Приморье'), ('Раздольное', 'Раздольное'), ('Светлана', 'Светлана'), ('Транспортная', 'Транспортная'), ('Тимерязева', 'Тимирязева'), ('Фабрициуса', 'Фабрициуса'), ('Хоста', 'Хоста'), ('Центр', 'Центр')], max_length=45, verbose_name='Район:'),
        ),
        migrations.AlterField(
            model_name='uchastok',
            name='status_obj',
            field=models.CharField(choices=[('Опубликован', 'Опубликован'), ('Не опубликован', 'Не опубликован')], max_length=45, verbose_name='Публикация обьекта'),
        ),
    ]
