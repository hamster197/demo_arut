# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-26 10:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0060_auto_20180323_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otchet_nov',
            name='reelt1',
            field=models.CharField(blank=True, choices=[('demo', 'demon demo'), ('alekseevau', 'Алексеева Юлия'), ('vishnevskiya', 'Вишневецкий Александр'), ('golovind', 'Головин Дмитрий'), ('deminaa', 'Демина Анжелика'), ('ujashakueva', 'Джашакуева Римма'), ('homka', 'Домников Роман'), ('aegorova', 'Егорова Анжелика'), ('ermolovat', 'Ермолова Татьяна'), ('refremov', 'Ефремов Руслан'), ('jarkovan', 'Жаркова Наталья'), ('gukovau', 'Жукова Юлия'), ('gukovaa', 'Жукова Анна'), ('zabolotiya', 'Заболотный Алексей'), ('zabolotiyd', 'Заболотный Дмитрий'), ('zalubivskiya', 'Залюбовский Алексей'), ('ivashenko', 'Иващенко Алексей'), ('livina', 'Ильина Людмила'), ('kazancevaa', 'Казанцева Анастасия'), ('mkaskov', 'Касков Максим'), ('klimovaf', 'Климкова Валентина'), ('kolesnika', 'Колесник Алина'), ('kondratovf', 'Кондратов Алексей'), ('crutihinao', 'Крутихина Ольга'), ('kuznecova', 'Кузнецов Алексей'), ('leontevd', 'Леонтьев Дмитрий'), ('liminae', 'Лимина Елена'), ('makarovam', 'Макарова Марина'), ('maslovam', 'Маслова Марина'), ('maskarao', 'Машкара Оксана'), ('melnichenkon', 'Мельничук Наталья'), ('resep', 'Менеджер Офис'), ('milovanovv', 'Милованов Виктор'), ('misarovak', 'Мисарова Кристина'), ('mihailova', 'Михайлов Антон'), ('mihailovau', 'Михайлова Юлия'), ('rnovikov', 'Новиков Роман'), ('novikove', 'Новиков Евгений'), ('novsyanikova', 'Овсянникова Нина'), ('odabashyane', 'Одабащьян Эдуард'), ('vorinchin', 'Оринчин Владимир'), ('pavlenkoa', 'Павленко Анастасия'), ('panasyka', 'Панасюк Александр'), ('paninv', 'Панин Владислав'), ('rpoluvyanov', 'Полувьянов Роман'), ('rudnevae', 'Руднева Елена'), ('savelevv', 'Савельев Евгений'), ('samodelova', 'Самоделов Андрей'), ('samodelovao', 'Самоделова Ольга'), ('samoryadova', 'Саморядов Андрей'), ('skripkinaa', 'Скрипкина Анастасия'), ('slavinskayat', 'Славинская Татьяна'), ('isolovova', 'Соловьева Инна'), ('nsolovova', 'Соловьева Наталья'), ('stasukv', 'Стасюк Вячеслав'), ('stepanovao', 'Степанова Ольга'), ('stringinai', 'Стрыгина Ирина'), ('surgutskayao', 'Сургутская Оксана'), ('tretuake', 'Третяк Евгений'), ('tyrins', 'Тюрин Сергей'), ('fomine', 'Фомин Евгений'), ('cipurdeyo', 'Ципурдей Олег'), ('shalimovav', 'Шалимова Виктория'), ('shatskayan', 'Шацкая Наталья'), ('strikovv', 'Штрыков Владислав'), ('shtrikovi', 'Штрыков Игорь'), ('yaglova', 'Яглов Алексей')], default=' ', help_text='Необязательно к заполнению', max_length=100, verbose_name='Риелтор в сделке №1'),
        ),
        migrations.AlterField(
            model_name='otchet_nov',
            name='reelt10',
            field=models.CharField(blank=True, choices=[('demo', 'demon demo'), ('alekseevau', 'Алексеева Юлия'), ('vishnevskiya', 'Вишневецкий Александр'), ('golovind', 'Головин Дмитрий'), ('deminaa', 'Демина Анжелика'), ('ujashakueva', 'Джашакуева Римма'), ('homka', 'Домников Роман'), ('aegorova', 'Егорова Анжелика'), ('ermolovat', 'Ермолова Татьяна'), ('refremov', 'Ефремов Руслан'), ('jarkovan', 'Жаркова Наталья'), ('gukovau', 'Жукова Юлия'), ('gukovaa', 'Жукова Анна'), ('zabolotiya', 'Заболотный Алексей'), ('zabolotiyd', 'Заболотный Дмитрий'), ('zalubivskiya', 'Залюбовский Алексей'), ('ivashenko', 'Иващенко Алексей'), ('livina', 'Ильина Людмила'), ('kazancevaa', 'Казанцева Анастасия'), ('mkaskov', 'Касков Максим'), ('klimovaf', 'Климкова Валентина'), ('kolesnika', 'Колесник Алина'), ('kondratovf', 'Кондратов Алексей'), ('crutihinao', 'Крутихина Ольга'), ('kuznecova', 'Кузнецов Алексей'), ('leontevd', 'Леонтьев Дмитрий'), ('liminae', 'Лимина Елена'), ('makarovam', 'Макарова Марина'), ('maslovam', 'Маслова Марина'), ('maskarao', 'Машкара Оксана'), ('melnichenkon', 'Мельничук Наталья'), ('resep', 'Менеджер Офис'), ('milovanovv', 'Милованов Виктор'), ('misarovak', 'Мисарова Кристина'), ('mihailova', 'Михайлов Антон'), ('mihailovau', 'Михайлова Юлия'), ('rnovikov', 'Новиков Роман'), ('novikove', 'Новиков Евгений'), ('novsyanikova', 'Овсянникова Нина'), ('odabashyane', 'Одабащьян Эдуард'), ('vorinchin', 'Оринчин Владимир'), ('pavlenkoa', 'Павленко Анастасия'), ('panasyka', 'Панасюк Александр'), ('paninv', 'Панин Владислав'), ('rpoluvyanov', 'Полувьянов Роман'), ('rudnevae', 'Руднева Елена'), ('savelevv', 'Савельев Евгений'), ('samodelova', 'Самоделов Андрей'), ('samodelovao', 'Самоделова Ольга'), ('samoryadova', 'Саморядов Андрей'), ('skripkinaa', 'Скрипкина Анастасия'), ('slavinskayat', 'Славинская Татьяна'), ('isolovova', 'Соловьева Инна'), ('nsolovova', 'Соловьева Наталья'), ('stasukv', 'Стасюк Вячеслав'), ('stepanovao', 'Степанова Ольга'), ('stringinai', 'Стрыгина Ирина'), ('surgutskayao', 'Сургутская Оксана'), ('tretuake', 'Третяк Евгений'), ('tyrins', 'Тюрин Сергей'), ('fomine', 'Фомин Евгений'), ('cipurdeyo', 'Ципурдей Олег'), ('shalimovav', 'Шалимова Виктория'), ('shatskayan', 'Шацкая Наталья'), ('strikovv', 'Штрыков Владислав'), ('shtrikovi', 'Штрыков Игорь'), ('yaglova', 'Яглов Алексей')], default=' ', help_text='Необязательно к заполнению', max_length=100, verbose_name='Риелтор в сделке №10'),
        ),
        migrations.AlterField(
            model_name='otchet_nov',
            name='reelt2',
            field=models.CharField(blank=True, choices=[('demo', 'demon demo'), ('alekseevau', 'Алексеева Юлия'), ('vishnevskiya', 'Вишневецкий Александр'), ('golovind', 'Головин Дмитрий'), ('deminaa', 'Демина Анжелика'), ('ujashakueva', 'Джашакуева Римма'), ('homka', 'Домников Роман'), ('aegorova', 'Егорова Анжелика'), ('ermolovat', 'Ермолова Татьяна'), ('refremov', 'Ефремов Руслан'), ('jarkovan', 'Жаркова Наталья'), ('gukovau', 'Жукова Юлия'), ('gukovaa', 'Жукова Анна'), ('zabolotiya', 'Заболотный Алексей'), ('zabolotiyd', 'Заболотный Дмитрий'), ('zalubivskiya', 'Залюбовский Алексей'), ('ivashenko', 'Иващенко Алексей'), ('livina', 'Ильина Людмила'), ('kazancevaa', 'Казанцева Анастасия'), ('mkaskov', 'Касков Максим'), ('klimovaf', 'Климкова Валентина'), ('kolesnika', 'Колесник Алина'), ('kondratovf', 'Кондратов Алексей'), ('crutihinao', 'Крутихина Ольга'), ('kuznecova', 'Кузнецов Алексей'), ('leontevd', 'Леонтьев Дмитрий'), ('liminae', 'Лимина Елена'), ('makarovam', 'Макарова Марина'), ('maslovam', 'Маслова Марина'), ('maskarao', 'Машкара Оксана'), ('melnichenkon', 'Мельничук Наталья'), ('resep', 'Менеджер Офис'), ('milovanovv', 'Милованов Виктор'), ('misarovak', 'Мисарова Кристина'), ('mihailova', 'Михайлов Антон'), ('mihailovau', 'Михайлова Юлия'), ('rnovikov', 'Новиков Роман'), ('novikove', 'Новиков Евгений'), ('novsyanikova', 'Овсянникова Нина'), ('odabashyane', 'Одабащьян Эдуард'), ('vorinchin', 'Оринчин Владимир'), ('pavlenkoa', 'Павленко Анастасия'), ('panasyka', 'Панасюк Александр'), ('paninv', 'Панин Владислав'), ('rpoluvyanov', 'Полувьянов Роман'), ('rudnevae', 'Руднева Елена'), ('savelevv', 'Савельев Евгений'), ('samodelova', 'Самоделов Андрей'), ('samodelovao', 'Самоделова Ольга'), ('samoryadova', 'Саморядов Андрей'), ('skripkinaa', 'Скрипкина Анастасия'), ('slavinskayat', 'Славинская Татьяна'), ('isolovova', 'Соловьева Инна'), ('nsolovova', 'Соловьева Наталья'), ('stasukv', 'Стасюк Вячеслав'), ('stepanovao', 'Степанова Ольга'), ('stringinai', 'Стрыгина Ирина'), ('surgutskayao', 'Сургутская Оксана'), ('tretuake', 'Третяк Евгений'), ('tyrins', 'Тюрин Сергей'), ('fomine', 'Фомин Евгений'), ('cipurdeyo', 'Ципурдей Олег'), ('shalimovav', 'Шалимова Виктория'), ('shatskayan', 'Шацкая Наталья'), ('strikovv', 'Штрыков Владислав'), ('shtrikovi', 'Штрыков Игорь'), ('yaglova', 'Яглов Алексей')], default=' ', help_text='Необязательно к заполнению', max_length=100, verbose_name='Риелтор в сделке №2'),
        ),
        migrations.AlterField(
            model_name='otchet_nov',
            name='reelt3',
            field=models.CharField(blank=True, choices=[('demo', 'demon demo'), ('alekseevau', 'Алексеева Юлия'), ('vishnevskiya', 'Вишневецкий Александр'), ('golovind', 'Головин Дмитрий'), ('deminaa', 'Демина Анжелика'), ('ujashakueva', 'Джашакуева Римма'), ('homka', 'Домников Роман'), ('aegorova', 'Егорова Анжелика'), ('ermolovat', 'Ермолова Татьяна'), ('refremov', 'Ефремов Руслан'), ('jarkovan', 'Жаркова Наталья'), ('gukovau', 'Жукова Юлия'), ('gukovaa', 'Жукова Анна'), ('zabolotiya', 'Заболотный Алексей'), ('zabolotiyd', 'Заболотный Дмитрий'), ('zalubivskiya', 'Залюбовский Алексей'), ('ivashenko', 'Иващенко Алексей'), ('livina', 'Ильина Людмила'), ('kazancevaa', 'Казанцева Анастасия'), ('mkaskov', 'Касков Максим'), ('klimovaf', 'Климкова Валентина'), ('kolesnika', 'Колесник Алина'), ('kondratovf', 'Кондратов Алексей'), ('crutihinao', 'Крутихина Ольга'), ('kuznecova', 'Кузнецов Алексей'), ('leontevd', 'Леонтьев Дмитрий'), ('liminae', 'Лимина Елена'), ('makarovam', 'Макарова Марина'), ('maslovam', 'Маслова Марина'), ('maskarao', 'Машкара Оксана'), ('melnichenkon', 'Мельничук Наталья'), ('resep', 'Менеджер Офис'), ('milovanovv', 'Милованов Виктор'), ('misarovak', 'Мисарова Кристина'), ('mihailova', 'Михайлов Антон'), ('mihailovau', 'Михайлова Юлия'), ('rnovikov', 'Новиков Роман'), ('novikove', 'Новиков Евгений'), ('novsyanikova', 'Овсянникова Нина'), ('odabashyane', 'Одабащьян Эдуард'), ('vorinchin', 'Оринчин Владимир'), ('pavlenkoa', 'Павленко Анастасия'), ('panasyka', 'Панасюк Александр'), ('paninv', 'Панин Владислав'), ('rpoluvyanov', 'Полувьянов Роман'), ('rudnevae', 'Руднева Елена'), ('savelevv', 'Савельев Евгений'), ('samodelova', 'Самоделов Андрей'), ('samodelovao', 'Самоделова Ольга'), ('samoryadova', 'Саморядов Андрей'), ('skripkinaa', 'Скрипкина Анастасия'), ('slavinskayat', 'Славинская Татьяна'), ('isolovova', 'Соловьева Инна'), ('nsolovova', 'Соловьева Наталья'), ('stasukv', 'Стасюк Вячеслав'), ('stepanovao', 'Степанова Ольга'), ('stringinai', 'Стрыгина Ирина'), ('surgutskayao', 'Сургутская Оксана'), ('tretuake', 'Третяк Евгений'), ('tyrins', 'Тюрин Сергей'), ('fomine', 'Фомин Евгений'), ('cipurdeyo', 'Ципурдей Олег'), ('shalimovav', 'Шалимова Виктория'), ('shatskayan', 'Шацкая Наталья'), ('strikovv', 'Штрыков Владислав'), ('shtrikovi', 'Штрыков Игорь'), ('yaglova', 'Яглов Алексей')], default=' ', help_text='Необязательно к заполнению', max_length=100, verbose_name='Риелтор в сделке №3'),
        ),
        migrations.AlterField(
            model_name='otchet_nov',
            name='reelt4',
            field=models.CharField(blank=True, choices=[('demo', 'demon demo'), ('alekseevau', 'Алексеева Юлия'), ('vishnevskiya', 'Вишневецкий Александр'), ('golovind', 'Головин Дмитрий'), ('deminaa', 'Демина Анжелика'), ('ujashakueva', 'Джашакуева Римма'), ('homka', 'Домников Роман'), ('aegorova', 'Егорова Анжелика'), ('ermolovat', 'Ермолова Татьяна'), ('refremov', 'Ефремов Руслан'), ('jarkovan', 'Жаркова Наталья'), ('gukovau', 'Жукова Юлия'), ('gukovaa', 'Жукова Анна'), ('zabolotiya', 'Заболотный Алексей'), ('zabolotiyd', 'Заболотный Дмитрий'), ('zalubivskiya', 'Залюбовский Алексей'), ('ivashenko', 'Иващенко Алексей'), ('livina', 'Ильина Людмила'), ('kazancevaa', 'Казанцева Анастасия'), ('mkaskov', 'Касков Максим'), ('klimovaf', 'Климкова Валентина'), ('kolesnika', 'Колесник Алина'), ('kondratovf', 'Кондратов Алексей'), ('crutihinao', 'Крутихина Ольга'), ('kuznecova', 'Кузнецов Алексей'), ('leontevd', 'Леонтьев Дмитрий'), ('liminae', 'Лимина Елена'), ('makarovam', 'Макарова Марина'), ('maslovam', 'Маслова Марина'), ('maskarao', 'Машкара Оксана'), ('melnichenkon', 'Мельничук Наталья'), ('resep', 'Менеджер Офис'), ('milovanovv', 'Милованов Виктор'), ('misarovak', 'Мисарова Кристина'), ('mihailova', 'Михайлов Антон'), ('mihailovau', 'Михайлова Юлия'), ('rnovikov', 'Новиков Роман'), ('novikove', 'Новиков Евгений'), ('novsyanikova', 'Овсянникова Нина'), ('odabashyane', 'Одабащьян Эдуард'), ('vorinchin', 'Оринчин Владимир'), ('pavlenkoa', 'Павленко Анастасия'), ('panasyka', 'Панасюк Александр'), ('paninv', 'Панин Владислав'), ('rpoluvyanov', 'Полувьянов Роман'), ('rudnevae', 'Руднева Елена'), ('savelevv', 'Савельев Евгений'), ('samodelova', 'Самоделов Андрей'), ('samodelovao', 'Самоделова Ольга'), ('samoryadova', 'Саморядов Андрей'), ('skripkinaa', 'Скрипкина Анастасия'), ('slavinskayat', 'Славинская Татьяна'), ('isolovova', 'Соловьева Инна'), ('nsolovova', 'Соловьева Наталья'), ('stasukv', 'Стасюк Вячеслав'), ('stepanovao', 'Степанова Ольга'), ('stringinai', 'Стрыгина Ирина'), ('surgutskayao', 'Сургутская Оксана'), ('tretuake', 'Третяк Евгений'), ('tyrins', 'Тюрин Сергей'), ('fomine', 'Фомин Евгений'), ('cipurdeyo', 'Ципурдей Олег'), ('shalimovav', 'Шалимова Виктория'), ('shatskayan', 'Шацкая Наталья'), ('strikovv', 'Штрыков Владислав'), ('shtrikovi', 'Штрыков Игорь'), ('yaglova', 'Яглов Алексей')], default=' ', help_text='Необязательно к заполнению', max_length=100, verbose_name='Риелтор в сделке №4'),
        ),
        migrations.AlterField(
            model_name='otchet_nov',
            name='reelt5',
            field=models.CharField(blank=True, choices=[('demo', 'demon demo'), ('alekseevau', 'Алексеева Юлия'), ('vishnevskiya', 'Вишневецкий Александр'), ('golovind', 'Головин Дмитрий'), ('deminaa', 'Демина Анжелика'), ('ujashakueva', 'Джашакуева Римма'), ('homka', 'Домников Роман'), ('aegorova', 'Егорова Анжелика'), ('ermolovat', 'Ермолова Татьяна'), ('refremov', 'Ефремов Руслан'), ('jarkovan', 'Жаркова Наталья'), ('gukovau', 'Жукова Юлия'), ('gukovaa', 'Жукова Анна'), ('zabolotiya', 'Заболотный Алексей'), ('zabolotiyd', 'Заболотный Дмитрий'), ('zalubivskiya', 'Залюбовский Алексей'), ('ivashenko', 'Иващенко Алексей'), ('livina', 'Ильина Людмила'), ('kazancevaa', 'Казанцева Анастасия'), ('mkaskov', 'Касков Максим'), ('klimovaf', 'Климкова Валентина'), ('kolesnika', 'Колесник Алина'), ('kondratovf', 'Кондратов Алексей'), ('crutihinao', 'Крутихина Ольга'), ('kuznecova', 'Кузнецов Алексей'), ('leontevd', 'Леонтьев Дмитрий'), ('liminae', 'Лимина Елена'), ('makarovam', 'Макарова Марина'), ('maslovam', 'Маслова Марина'), ('maskarao', 'Машкара Оксана'), ('melnichenkon', 'Мельничук Наталья'), ('resep', 'Менеджер Офис'), ('milovanovv', 'Милованов Виктор'), ('misarovak', 'Мисарова Кристина'), ('mihailova', 'Михайлов Антон'), ('mihailovau', 'Михайлова Юлия'), ('rnovikov', 'Новиков Роман'), ('novikove', 'Новиков Евгений'), ('novsyanikova', 'Овсянникова Нина'), ('odabashyane', 'Одабащьян Эдуард'), ('vorinchin', 'Оринчин Владимир'), ('pavlenkoa', 'Павленко Анастасия'), ('panasyka', 'Панасюк Александр'), ('paninv', 'Панин Владислав'), ('rpoluvyanov', 'Полувьянов Роман'), ('rudnevae', 'Руднева Елена'), ('savelevv', 'Савельев Евгений'), ('samodelova', 'Самоделов Андрей'), ('samodelovao', 'Самоделова Ольга'), ('samoryadova', 'Саморядов Андрей'), ('skripkinaa', 'Скрипкина Анастасия'), ('slavinskayat', 'Славинская Татьяна'), ('isolovova', 'Соловьева Инна'), ('nsolovova', 'Соловьева Наталья'), ('stasukv', 'Стасюк Вячеслав'), ('stepanovao', 'Степанова Ольга'), ('stringinai', 'Стрыгина Ирина'), ('surgutskayao', 'Сургутская Оксана'), ('tretuake', 'Третяк Евгений'), ('tyrins', 'Тюрин Сергей'), ('fomine', 'Фомин Евгений'), ('cipurdeyo', 'Ципурдей Олег'), ('shalimovav', 'Шалимова Виктория'), ('shatskayan', 'Шацкая Наталья'), ('strikovv', 'Штрыков Владислав'), ('shtrikovi', 'Штрыков Игорь'), ('yaglova', 'Яглов Алексей')], default=' ', help_text='Необязательно к заполнению', max_length=100, verbose_name='Риелтор в сделке №5'),
        ),
        migrations.AlterField(
            model_name='otchet_nov',
            name='reelt6',
            field=models.CharField(blank=True, choices=[('demo', 'demon demo'), ('alekseevau', 'Алексеева Юлия'), ('vishnevskiya', 'Вишневецкий Александр'), ('golovind', 'Головин Дмитрий'), ('deminaa', 'Демина Анжелика'), ('ujashakueva', 'Джашакуева Римма'), ('homka', 'Домников Роман'), ('aegorova', 'Егорова Анжелика'), ('ermolovat', 'Ермолова Татьяна'), ('refremov', 'Ефремов Руслан'), ('jarkovan', 'Жаркова Наталья'), ('gukovau', 'Жукова Юлия'), ('gukovaa', 'Жукова Анна'), ('zabolotiya', 'Заболотный Алексей'), ('zabolotiyd', 'Заболотный Дмитрий'), ('zalubivskiya', 'Залюбовский Алексей'), ('ivashenko', 'Иващенко Алексей'), ('livina', 'Ильина Людмила'), ('kazancevaa', 'Казанцева Анастасия'), ('mkaskov', 'Касков Максим'), ('klimovaf', 'Климкова Валентина'), ('kolesnika', 'Колесник Алина'), ('kondratovf', 'Кондратов Алексей'), ('crutihinao', 'Крутихина Ольга'), ('kuznecova', 'Кузнецов Алексей'), ('leontevd', 'Леонтьев Дмитрий'), ('liminae', 'Лимина Елена'), ('makarovam', 'Макарова Марина'), ('maslovam', 'Маслова Марина'), ('maskarao', 'Машкара Оксана'), ('melnichenkon', 'Мельничук Наталья'), ('resep', 'Менеджер Офис'), ('milovanovv', 'Милованов Виктор'), ('misarovak', 'Мисарова Кристина'), ('mihailova', 'Михайлов Антон'), ('mihailovau', 'Михайлова Юлия'), ('rnovikov', 'Новиков Роман'), ('novikove', 'Новиков Евгений'), ('novsyanikova', 'Овсянникова Нина'), ('odabashyane', 'Одабащьян Эдуард'), ('vorinchin', 'Оринчин Владимир'), ('pavlenkoa', 'Павленко Анастасия'), ('panasyka', 'Панасюк Александр'), ('paninv', 'Панин Владислав'), ('rpoluvyanov', 'Полувьянов Роман'), ('rudnevae', 'Руднева Елена'), ('savelevv', 'Савельев Евгений'), ('samodelova', 'Самоделов Андрей'), ('samodelovao', 'Самоделова Ольга'), ('samoryadova', 'Саморядов Андрей'), ('skripkinaa', 'Скрипкина Анастасия'), ('slavinskayat', 'Славинская Татьяна'), ('isolovova', 'Соловьева Инна'), ('nsolovova', 'Соловьева Наталья'), ('stasukv', 'Стасюк Вячеслав'), ('stepanovao', 'Степанова Ольга'), ('stringinai', 'Стрыгина Ирина'), ('surgutskayao', 'Сургутская Оксана'), ('tretuake', 'Третяк Евгений'), ('tyrins', 'Тюрин Сергей'), ('fomine', 'Фомин Евгений'), ('cipurdeyo', 'Ципурдей Олег'), ('shalimovav', 'Шалимова Виктория'), ('shatskayan', 'Шацкая Наталья'), ('strikovv', 'Штрыков Владислав'), ('shtrikovi', 'Штрыков Игорь'), ('yaglova', 'Яглов Алексей')], default=' ', help_text='Необязательно к заполнению', max_length=100, verbose_name='Риелтор в сделке №6'),
        ),
        migrations.AlterField(
            model_name='otchet_nov',
            name='reelt7',
            field=models.CharField(blank=True, choices=[('demo', 'demon demo'), ('alekseevau', 'Алексеева Юлия'), ('vishnevskiya', 'Вишневецкий Александр'), ('golovind', 'Головин Дмитрий'), ('deminaa', 'Демина Анжелика'), ('ujashakueva', 'Джашакуева Римма'), ('homka', 'Домников Роман'), ('aegorova', 'Егорова Анжелика'), ('ermolovat', 'Ермолова Татьяна'), ('refremov', 'Ефремов Руслан'), ('jarkovan', 'Жаркова Наталья'), ('gukovau', 'Жукова Юлия'), ('gukovaa', 'Жукова Анна'), ('zabolotiya', 'Заболотный Алексей'), ('zabolotiyd', 'Заболотный Дмитрий'), ('zalubivskiya', 'Залюбовский Алексей'), ('ivashenko', 'Иващенко Алексей'), ('livina', 'Ильина Людмила'), ('kazancevaa', 'Казанцева Анастасия'), ('mkaskov', 'Касков Максим'), ('klimovaf', 'Климкова Валентина'), ('kolesnika', 'Колесник Алина'), ('kondratovf', 'Кондратов Алексей'), ('crutihinao', 'Крутихина Ольга'), ('kuznecova', 'Кузнецов Алексей'), ('leontevd', 'Леонтьев Дмитрий'), ('liminae', 'Лимина Елена'), ('makarovam', 'Макарова Марина'), ('maslovam', 'Маслова Марина'), ('maskarao', 'Машкара Оксана'), ('melnichenkon', 'Мельничук Наталья'), ('resep', 'Менеджер Офис'), ('milovanovv', 'Милованов Виктор'), ('misarovak', 'Мисарова Кристина'), ('mihailova', 'Михайлов Антон'), ('mihailovau', 'Михайлова Юлия'), ('rnovikov', 'Новиков Роман'), ('novikove', 'Новиков Евгений'), ('novsyanikova', 'Овсянникова Нина'), ('odabashyane', 'Одабащьян Эдуард'), ('vorinchin', 'Оринчин Владимир'), ('pavlenkoa', 'Павленко Анастасия'), ('panasyka', 'Панасюк Александр'), ('paninv', 'Панин Владислав'), ('rpoluvyanov', 'Полувьянов Роман'), ('rudnevae', 'Руднева Елена'), ('savelevv', 'Савельев Евгений'), ('samodelova', 'Самоделов Андрей'), ('samodelovao', 'Самоделова Ольга'), ('samoryadova', 'Саморядов Андрей'), ('skripkinaa', 'Скрипкина Анастасия'), ('slavinskayat', 'Славинская Татьяна'), ('isolovova', 'Соловьева Инна'), ('nsolovova', 'Соловьева Наталья'), ('stasukv', 'Стасюк Вячеслав'), ('stepanovao', 'Степанова Ольга'), ('stringinai', 'Стрыгина Ирина'), ('surgutskayao', 'Сургутская Оксана'), ('tretuake', 'Третяк Евгений'), ('tyrins', 'Тюрин Сергей'), ('fomine', 'Фомин Евгений'), ('cipurdeyo', 'Ципурдей Олег'), ('shalimovav', 'Шалимова Виктория'), ('shatskayan', 'Шацкая Наталья'), ('strikovv', 'Штрыков Владислав'), ('shtrikovi', 'Штрыков Игорь'), ('yaglova', 'Яглов Алексей')], default=' ', help_text='Необязательно к заполнению', max_length=100, verbose_name='Риелтор в сделке №7'),
        ),
        migrations.AlterField(
            model_name='otchet_nov',
            name='reelt8',
            field=models.CharField(blank=True, choices=[('demo', 'demon demo'), ('alekseevau', 'Алексеева Юлия'), ('vishnevskiya', 'Вишневецкий Александр'), ('golovind', 'Головин Дмитрий'), ('deminaa', 'Демина Анжелика'), ('ujashakueva', 'Джашакуева Римма'), ('homka', 'Домников Роман'), ('aegorova', 'Егорова Анжелика'), ('ermolovat', 'Ермолова Татьяна'), ('refremov', 'Ефремов Руслан'), ('jarkovan', 'Жаркова Наталья'), ('gukovau', 'Жукова Юлия'), ('gukovaa', 'Жукова Анна'), ('zabolotiya', 'Заболотный Алексей'), ('zabolotiyd', 'Заболотный Дмитрий'), ('zalubivskiya', 'Залюбовский Алексей'), ('ivashenko', 'Иващенко Алексей'), ('livina', 'Ильина Людмила'), ('kazancevaa', 'Казанцева Анастасия'), ('mkaskov', 'Касков Максим'), ('klimovaf', 'Климкова Валентина'), ('kolesnika', 'Колесник Алина'), ('kondratovf', 'Кондратов Алексей'), ('crutihinao', 'Крутихина Ольга'), ('kuznecova', 'Кузнецов Алексей'), ('leontevd', 'Леонтьев Дмитрий'), ('liminae', 'Лимина Елена'), ('makarovam', 'Макарова Марина'), ('maslovam', 'Маслова Марина'), ('maskarao', 'Машкара Оксана'), ('melnichenkon', 'Мельничук Наталья'), ('resep', 'Менеджер Офис'), ('milovanovv', 'Милованов Виктор'), ('misarovak', 'Мисарова Кристина'), ('mihailova', 'Михайлов Антон'), ('mihailovau', 'Михайлова Юлия'), ('rnovikov', 'Новиков Роман'), ('novikove', 'Новиков Евгений'), ('novsyanikova', 'Овсянникова Нина'), ('odabashyane', 'Одабащьян Эдуард'), ('vorinchin', 'Оринчин Владимир'), ('pavlenkoa', 'Павленко Анастасия'), ('panasyka', 'Панасюк Александр'), ('paninv', 'Панин Владислав'), ('rpoluvyanov', 'Полувьянов Роман'), ('rudnevae', 'Руднева Елена'), ('savelevv', 'Савельев Евгений'), ('samodelova', 'Самоделов Андрей'), ('samodelovao', 'Самоделова Ольга'), ('samoryadova', 'Саморядов Андрей'), ('skripkinaa', 'Скрипкина Анастасия'), ('slavinskayat', 'Славинская Татьяна'), ('isolovova', 'Соловьева Инна'), ('nsolovova', 'Соловьева Наталья'), ('stasukv', 'Стасюк Вячеслав'), ('stepanovao', 'Степанова Ольга'), ('stringinai', 'Стрыгина Ирина'), ('surgutskayao', 'Сургутская Оксана'), ('tretuake', 'Третяк Евгений'), ('tyrins', 'Тюрин Сергей'), ('fomine', 'Фомин Евгений'), ('cipurdeyo', 'Ципурдей Олег'), ('shalimovav', 'Шалимова Виктория'), ('shatskayan', 'Шацкая Наталья'), ('strikovv', 'Штрыков Владислав'), ('shtrikovi', 'Штрыков Игорь'), ('yaglova', 'Яглов Алексей')], default=' ', help_text='Необязательно к заполнению', max_length=100, verbose_name='Риелтор в сделке №8'),
        ),
        migrations.AlterField(
            model_name='otchet_nov',
            name='reelt9',
            field=models.CharField(blank=True, choices=[('demo', 'demon demo'), ('alekseevau', 'Алексеева Юлия'), ('vishnevskiya', 'Вишневецкий Александр'), ('golovind', 'Головин Дмитрий'), ('deminaa', 'Демина Анжелика'), ('ujashakueva', 'Джашакуева Римма'), ('homka', 'Домников Роман'), ('aegorova', 'Егорова Анжелика'), ('ermolovat', 'Ермолова Татьяна'), ('refremov', 'Ефремов Руслан'), ('jarkovan', 'Жаркова Наталья'), ('gukovau', 'Жукова Юлия'), ('gukovaa', 'Жукова Анна'), ('zabolotiya', 'Заболотный Алексей'), ('zabolotiyd', 'Заболотный Дмитрий'), ('zalubivskiya', 'Залюбовский Алексей'), ('ivashenko', 'Иващенко Алексей'), ('livina', 'Ильина Людмила'), ('kazancevaa', 'Казанцева Анастасия'), ('mkaskov', 'Касков Максим'), ('klimovaf', 'Климкова Валентина'), ('kolesnika', 'Колесник Алина'), ('kondratovf', 'Кондратов Алексей'), ('crutihinao', 'Крутихина Ольга'), ('kuznecova', 'Кузнецов Алексей'), ('leontevd', 'Леонтьев Дмитрий'), ('liminae', 'Лимина Елена'), ('makarovam', 'Макарова Марина'), ('maslovam', 'Маслова Марина'), ('maskarao', 'Машкара Оксана'), ('melnichenkon', 'Мельничук Наталья'), ('resep', 'Менеджер Офис'), ('milovanovv', 'Милованов Виктор'), ('misarovak', 'Мисарова Кристина'), ('mihailova', 'Михайлов Антон'), ('mihailovau', 'Михайлова Юлия'), ('rnovikov', 'Новиков Роман'), ('novikove', 'Новиков Евгений'), ('novsyanikova', 'Овсянникова Нина'), ('odabashyane', 'Одабащьян Эдуард'), ('vorinchin', 'Оринчин Владимир'), ('pavlenkoa', 'Павленко Анастасия'), ('panasyka', 'Панасюк Александр'), ('paninv', 'Панин Владислав'), ('rpoluvyanov', 'Полувьянов Роман'), ('rudnevae', 'Руднева Елена'), ('savelevv', 'Савельев Евгений'), ('samodelova', 'Самоделов Андрей'), ('samodelovao', 'Самоделова Ольга'), ('samoryadova', 'Саморядов Андрей'), ('skripkinaa', 'Скрипкина Анастасия'), ('slavinskayat', 'Славинская Татьяна'), ('isolovova', 'Соловьева Инна'), ('nsolovova', 'Соловьева Наталья'), ('stasukv', 'Стасюк Вячеслав'), ('stepanovao', 'Степанова Ольга'), ('stringinai', 'Стрыгина Ирина'), ('surgutskayao', 'Сургутская Оксана'), ('tretuake', 'Третяк Евгений'), ('tyrins', 'Тюрин Сергей'), ('fomine', 'Фомин Евгений'), ('cipurdeyo', 'Ципурдей Олег'), ('shalimovav', 'Шалимова Виктория'), ('shatskayan', 'Шацкая Наталья'), ('strikovv', 'Штрыков Владислав'), ('shtrikovi', 'Штрыков Игорь'), ('yaglova', 'Яглов Алексей')], default=' ', help_text='Необязательно к заполнению', max_length=100, verbose_name='Риелтор в сделке №9'),
        ),
    ]
