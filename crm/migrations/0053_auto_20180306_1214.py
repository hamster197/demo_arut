# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-06 09:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0052_auto_20180302_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otchet_nov',
            name='reelt1',
            field=models.CharField(blank=True, choices=[('homka', 'Роман Домников'), ('demo', 'demo demon'), ('surgutskayao', 'Оксана Сургутская'), ('alekseevau', 'Юлия Алексеева'), ('crutihinao', 'Ольга Крутихина'), ('mihailovau', 'Юлия Михайлова'), ('samoryadova', 'Андрей Саморядов'), ('shalimovav', 'Виктория Шалимова'), ('skripkinaa', 'Анастасия Скрипкина'), ('odabashyane', 'Эдуард Одабащьян'), ('rnovikov', 'Роман Новиков'), ('ujashakueva', 'Римма Джашакуева'), ('refremov', 'Руслан Ефремов'), ('aegorova', 'Анжелика Егорова'), ('livina', 'Людмила Ильина'), ('mkaskov', 'Максим Касков'), ('vorinchin', 'Владимир Оринчин'), ('novsyanikova', 'Нина Овсянникова'), ('rpoluvyanov', 'Роман Полувьянов'), ('isolovova', 'Инна Соловьева'), ('nsolovova', 'Наталья Соловьева'), ('paninv', 'Владислав Панин'), ('leontevd', 'Дмитрий Леонтьев'), ('makarovam', 'Марина Макарова'), ('maslovam', 'Марина Маслова'), ('novikove', 'Евгений Новиков'), ('stasukv', 'Вячеслав Стасюк'), ('zabolotiya', 'Алексей Заболотный'), ('liminae', 'Елена Лимина'), ('panasyka', 'Александр Панасюк'), ('tyrins', 'Сергей Тюрин'), ('zabolotiyd', 'Дмитрий Заболотный'), ('ivashenko', 'Алексей Иващенко'), ('jarkovan', 'Наталья Жаркова'), ('kazancevaa', 'Анастасия Казанцева'), ('mihailova', 'Антон Михайлов'), ('panochkin', 'Виктор Паночкин'), ('samodelovao', 'Ольга Самоделова'), ('samodelova', 'Андрей Самоделов'), ('shatskayan', 'Наталья Шацкая'), ('shutenkoa', 'Антон Шутенко'), ('sukhobaevskayam', 'Марина Сухобаевская'), ('timofeevas', 'Светлана Тимофеева'), ('uldasheva', 'Андрей Юлдашев'), ('tretuake', 'Евгений Третяк'), ('stepanovao', 'Ольга Степанова'), ('gukovau', 'Юлия Жукова'), ('maskarao', 'Оксана Машкара'), ('ermolovat', 'Татьяна Ермолова'), ('chelyadinovao', 'Ольга Челядинова'), ('savickayai', 'Ирина Савицкая'), ('milovanovv', 'Виктор Милованов'), ('golovind', 'Дмитрий Головин'), ('rudnevae', 'Елена Руднева'), ('cipurdeyo', 'Олег Ципурдей'), ('yaglova', 'Алексей Яглов'), ('deminaa', 'Анжелика Демина'), ('vishnevskiya', 'Александр Вишневецкий'), ('gukovaa', 'Анна Жукова'), ('klimovaf', 'Валентина Климкова'), ('pavlenkoa', 'Анастасия Павленко'), ('slavinskayat', 'Татьяна Славинская'), ('strikovv', 'Владислав Штрыков'), ('shtrikovi', 'Игорь Штрыков'), ('kondratovf', 'Алексей Кондратов'), ('zalubivskiya', 'Алексей Залюбовский'), ('kuznecova', 'Алексей Кузнецов'), ('stringinai', 'Ирина Стрыгина'), ('kolesnika', 'Алина Колесник'), ('savelevv', 'Евгений Савельев'), ('melnichenkon', 'Наталья Мельничук'), ('resep', 'Офис Менеджер'), ('fomine', 'Евгений Фомин')], default=' ', help_text='Необязательно к заполнению', max_length=100, verbose_name='Риелтор в сделке №1'),
        ),
        migrations.AlterField(
            model_name='otchet_nov',
            name='reelt10',
            field=models.CharField(blank=True, choices=[('homka', 'Роман Домников'), ('demo', 'demo demon'), ('surgutskayao', 'Оксана Сургутская'), ('alekseevau', 'Юлия Алексеева'), ('crutihinao', 'Ольга Крутихина'), ('mihailovau', 'Юлия Михайлова'), ('samoryadova', 'Андрей Саморядов'), ('shalimovav', 'Виктория Шалимова'), ('skripkinaa', 'Анастасия Скрипкина'), ('odabashyane', 'Эдуард Одабащьян'), ('rnovikov', 'Роман Новиков'), ('ujashakueva', 'Римма Джашакуева'), ('refremov', 'Руслан Ефремов'), ('aegorova', 'Анжелика Егорова'), ('livina', 'Людмила Ильина'), ('mkaskov', 'Максим Касков'), ('vorinchin', 'Владимир Оринчин'), ('novsyanikova', 'Нина Овсянникова'), ('rpoluvyanov', 'Роман Полувьянов'), ('isolovova', 'Инна Соловьева'), ('nsolovova', 'Наталья Соловьева'), ('paninv', 'Владислав Панин'), ('leontevd', 'Дмитрий Леонтьев'), ('makarovam', 'Марина Макарова'), ('maslovam', 'Марина Маслова'), ('novikove', 'Евгений Новиков'), ('stasukv', 'Вячеслав Стасюк'), ('zabolotiya', 'Алексей Заболотный'), ('liminae', 'Елена Лимина'), ('panasyka', 'Александр Панасюк'), ('tyrins', 'Сергей Тюрин'), ('zabolotiyd', 'Дмитрий Заболотный'), ('ivashenko', 'Алексей Иващенко'), ('jarkovan', 'Наталья Жаркова'), ('kazancevaa', 'Анастасия Казанцева'), ('mihailova', 'Антон Михайлов'), ('panochkin', 'Виктор Паночкин'), ('samodelovao', 'Ольга Самоделова'), ('samodelova', 'Андрей Самоделов'), ('shatskayan', 'Наталья Шацкая'), ('shutenkoa', 'Антон Шутенко'), ('sukhobaevskayam', 'Марина Сухобаевская'), ('timofeevas', 'Светлана Тимофеева'), ('uldasheva', 'Андрей Юлдашев'), ('tretuake', 'Евгений Третяк'), ('stepanovao', 'Ольга Степанова'), ('gukovau', 'Юлия Жукова'), ('maskarao', 'Оксана Машкара'), ('ermolovat', 'Татьяна Ермолова'), ('chelyadinovao', 'Ольга Челядинова'), ('savickayai', 'Ирина Савицкая'), ('milovanovv', 'Виктор Милованов'), ('golovind', 'Дмитрий Головин'), ('rudnevae', 'Елена Руднева'), ('cipurdeyo', 'Олег Ципурдей'), ('yaglova', 'Алексей Яглов'), ('deminaa', 'Анжелика Демина'), ('vishnevskiya', 'Александр Вишневецкий'), ('gukovaa', 'Анна Жукова'), ('klimovaf', 'Валентина Климкова'), ('pavlenkoa', 'Анастасия Павленко'), ('slavinskayat', 'Татьяна Славинская'), ('strikovv', 'Владислав Штрыков'), ('shtrikovi', 'Игорь Штрыков'), ('kondratovf', 'Алексей Кондратов'), ('zalubivskiya', 'Алексей Залюбовский'), ('kuznecova', 'Алексей Кузнецов'), ('stringinai', 'Ирина Стрыгина'), ('kolesnika', 'Алина Колесник'), ('savelevv', 'Евгений Савельев'), ('melnichenkon', 'Наталья Мельничук'), ('resep', 'Офис Менеджер'), ('fomine', 'Евгений Фомин')], default=' ', help_text='Необязательно к заполнению', max_length=100, verbose_name='Риелтор в сделке №10'),
        ),
        migrations.AlterField(
            model_name='otchet_nov',
            name='reelt2',
            field=models.CharField(blank=True, choices=[('homka', 'Роман Домников'), ('demo', 'demo demon'), ('surgutskayao', 'Оксана Сургутская'), ('alekseevau', 'Юлия Алексеева'), ('crutihinao', 'Ольга Крутихина'), ('mihailovau', 'Юлия Михайлова'), ('samoryadova', 'Андрей Саморядов'), ('shalimovav', 'Виктория Шалимова'), ('skripkinaa', 'Анастасия Скрипкина'), ('odabashyane', 'Эдуард Одабащьян'), ('rnovikov', 'Роман Новиков'), ('ujashakueva', 'Римма Джашакуева'), ('refremov', 'Руслан Ефремов'), ('aegorova', 'Анжелика Егорова'), ('livina', 'Людмила Ильина'), ('mkaskov', 'Максим Касков'), ('vorinchin', 'Владимир Оринчин'), ('novsyanikova', 'Нина Овсянникова'), ('rpoluvyanov', 'Роман Полувьянов'), ('isolovova', 'Инна Соловьева'), ('nsolovova', 'Наталья Соловьева'), ('paninv', 'Владислав Панин'), ('leontevd', 'Дмитрий Леонтьев'), ('makarovam', 'Марина Макарова'), ('maslovam', 'Марина Маслова'), ('novikove', 'Евгений Новиков'), ('stasukv', 'Вячеслав Стасюк'), ('zabolotiya', 'Алексей Заболотный'), ('liminae', 'Елена Лимина'), ('panasyka', 'Александр Панасюк'), ('tyrins', 'Сергей Тюрин'), ('zabolotiyd', 'Дмитрий Заболотный'), ('ivashenko', 'Алексей Иващенко'), ('jarkovan', 'Наталья Жаркова'), ('kazancevaa', 'Анастасия Казанцева'), ('mihailova', 'Антон Михайлов'), ('panochkin', 'Виктор Паночкин'), ('samodelovao', 'Ольга Самоделова'), ('samodelova', 'Андрей Самоделов'), ('shatskayan', 'Наталья Шацкая'), ('shutenkoa', 'Антон Шутенко'), ('sukhobaevskayam', 'Марина Сухобаевская'), ('timofeevas', 'Светлана Тимофеева'), ('uldasheva', 'Андрей Юлдашев'), ('tretuake', 'Евгений Третяк'), ('stepanovao', 'Ольга Степанова'), ('gukovau', 'Юлия Жукова'), ('maskarao', 'Оксана Машкара'), ('ermolovat', 'Татьяна Ермолова'), ('chelyadinovao', 'Ольга Челядинова'), ('savickayai', 'Ирина Савицкая'), ('milovanovv', 'Виктор Милованов'), ('golovind', 'Дмитрий Головин'), ('rudnevae', 'Елена Руднева'), ('cipurdeyo', 'Олег Ципурдей'), ('yaglova', 'Алексей Яглов'), ('deminaa', 'Анжелика Демина'), ('vishnevskiya', 'Александр Вишневецкий'), ('gukovaa', 'Анна Жукова'), ('klimovaf', 'Валентина Климкова'), ('pavlenkoa', 'Анастасия Павленко'), ('slavinskayat', 'Татьяна Славинская'), ('strikovv', 'Владислав Штрыков'), ('shtrikovi', 'Игорь Штрыков'), ('kondratovf', 'Алексей Кондратов'), ('zalubivskiya', 'Алексей Залюбовский'), ('kuznecova', 'Алексей Кузнецов'), ('stringinai', 'Ирина Стрыгина'), ('kolesnika', 'Алина Колесник'), ('savelevv', 'Евгений Савельев'), ('melnichenkon', 'Наталья Мельничук'), ('resep', 'Офис Менеджер'), ('fomine', 'Евгений Фомин')], default=' ', help_text='Необязательно к заполнению', max_length=100, verbose_name='Риелтор в сделке №2'),
        ),
        migrations.AlterField(
            model_name='otchet_nov',
            name='reelt3',
            field=models.CharField(blank=True, choices=[('homka', 'Роман Домников'), ('demo', 'demo demon'), ('surgutskayao', 'Оксана Сургутская'), ('alekseevau', 'Юлия Алексеева'), ('crutihinao', 'Ольга Крутихина'), ('mihailovau', 'Юлия Михайлова'), ('samoryadova', 'Андрей Саморядов'), ('shalimovav', 'Виктория Шалимова'), ('skripkinaa', 'Анастасия Скрипкина'), ('odabashyane', 'Эдуард Одабащьян'), ('rnovikov', 'Роман Новиков'), ('ujashakueva', 'Римма Джашакуева'), ('refremov', 'Руслан Ефремов'), ('aegorova', 'Анжелика Егорова'), ('livina', 'Людмила Ильина'), ('mkaskov', 'Максим Касков'), ('vorinchin', 'Владимир Оринчин'), ('novsyanikova', 'Нина Овсянникова'), ('rpoluvyanov', 'Роман Полувьянов'), ('isolovova', 'Инна Соловьева'), ('nsolovova', 'Наталья Соловьева'), ('paninv', 'Владислав Панин'), ('leontevd', 'Дмитрий Леонтьев'), ('makarovam', 'Марина Макарова'), ('maslovam', 'Марина Маслова'), ('novikove', 'Евгений Новиков'), ('stasukv', 'Вячеслав Стасюк'), ('zabolotiya', 'Алексей Заболотный'), ('liminae', 'Елена Лимина'), ('panasyka', 'Александр Панасюк'), ('tyrins', 'Сергей Тюрин'), ('zabolotiyd', 'Дмитрий Заболотный'), ('ivashenko', 'Алексей Иващенко'), ('jarkovan', 'Наталья Жаркова'), ('kazancevaa', 'Анастасия Казанцева'), ('mihailova', 'Антон Михайлов'), ('panochkin', 'Виктор Паночкин'), ('samodelovao', 'Ольга Самоделова'), ('samodelova', 'Андрей Самоделов'), ('shatskayan', 'Наталья Шацкая'), ('shutenkoa', 'Антон Шутенко'), ('sukhobaevskayam', 'Марина Сухобаевская'), ('timofeevas', 'Светлана Тимофеева'), ('uldasheva', 'Андрей Юлдашев'), ('tretuake', 'Евгений Третяк'), ('stepanovao', 'Ольга Степанова'), ('gukovau', 'Юлия Жукова'), ('maskarao', 'Оксана Машкара'), ('ermolovat', 'Татьяна Ермолова'), ('chelyadinovao', 'Ольга Челядинова'), ('savickayai', 'Ирина Савицкая'), ('milovanovv', 'Виктор Милованов'), ('golovind', 'Дмитрий Головин'), ('rudnevae', 'Елена Руднева'), ('cipurdeyo', 'Олег Ципурдей'), ('yaglova', 'Алексей Яглов'), ('deminaa', 'Анжелика Демина'), ('vishnevskiya', 'Александр Вишневецкий'), ('gukovaa', 'Анна Жукова'), ('klimovaf', 'Валентина Климкова'), ('pavlenkoa', 'Анастасия Павленко'), ('slavinskayat', 'Татьяна Славинская'), ('strikovv', 'Владислав Штрыков'), ('shtrikovi', 'Игорь Штрыков'), ('kondratovf', 'Алексей Кондратов'), ('zalubivskiya', 'Алексей Залюбовский'), ('kuznecova', 'Алексей Кузнецов'), ('stringinai', 'Ирина Стрыгина'), ('kolesnika', 'Алина Колесник'), ('savelevv', 'Евгений Савельев'), ('melnichenkon', 'Наталья Мельничук'), ('resep', 'Офис Менеджер'), ('fomine', 'Евгений Фомин')], default=' ', help_text='Необязательно к заполнению', max_length=100, verbose_name='Риелтор в сделке №3'),
        ),
        migrations.AlterField(
            model_name='otchet_nov',
            name='reelt4',
            field=models.CharField(blank=True, choices=[('homka', 'Роман Домников'), ('demo', 'demo demon'), ('surgutskayao', 'Оксана Сургутская'), ('alekseevau', 'Юлия Алексеева'), ('crutihinao', 'Ольга Крутихина'), ('mihailovau', 'Юлия Михайлова'), ('samoryadova', 'Андрей Саморядов'), ('shalimovav', 'Виктория Шалимова'), ('skripkinaa', 'Анастасия Скрипкина'), ('odabashyane', 'Эдуард Одабащьян'), ('rnovikov', 'Роман Новиков'), ('ujashakueva', 'Римма Джашакуева'), ('refremov', 'Руслан Ефремов'), ('aegorova', 'Анжелика Егорова'), ('livina', 'Людмила Ильина'), ('mkaskov', 'Максим Касков'), ('vorinchin', 'Владимир Оринчин'), ('novsyanikova', 'Нина Овсянникова'), ('rpoluvyanov', 'Роман Полувьянов'), ('isolovova', 'Инна Соловьева'), ('nsolovova', 'Наталья Соловьева'), ('paninv', 'Владислав Панин'), ('leontevd', 'Дмитрий Леонтьев'), ('makarovam', 'Марина Макарова'), ('maslovam', 'Марина Маслова'), ('novikove', 'Евгений Новиков'), ('stasukv', 'Вячеслав Стасюк'), ('zabolotiya', 'Алексей Заболотный'), ('liminae', 'Елена Лимина'), ('panasyka', 'Александр Панасюк'), ('tyrins', 'Сергей Тюрин'), ('zabolotiyd', 'Дмитрий Заболотный'), ('ivashenko', 'Алексей Иващенко'), ('jarkovan', 'Наталья Жаркова'), ('kazancevaa', 'Анастасия Казанцева'), ('mihailova', 'Антон Михайлов'), ('panochkin', 'Виктор Паночкин'), ('samodelovao', 'Ольга Самоделова'), ('samodelova', 'Андрей Самоделов'), ('shatskayan', 'Наталья Шацкая'), ('shutenkoa', 'Антон Шутенко'), ('sukhobaevskayam', 'Марина Сухобаевская'), ('timofeevas', 'Светлана Тимофеева'), ('uldasheva', 'Андрей Юлдашев'), ('tretuake', 'Евгений Третяк'), ('stepanovao', 'Ольга Степанова'), ('gukovau', 'Юлия Жукова'), ('maskarao', 'Оксана Машкара'), ('ermolovat', 'Татьяна Ермолова'), ('chelyadinovao', 'Ольга Челядинова'), ('savickayai', 'Ирина Савицкая'), ('milovanovv', 'Виктор Милованов'), ('golovind', 'Дмитрий Головин'), ('rudnevae', 'Елена Руднева'), ('cipurdeyo', 'Олег Ципурдей'), ('yaglova', 'Алексей Яглов'), ('deminaa', 'Анжелика Демина'), ('vishnevskiya', 'Александр Вишневецкий'), ('gukovaa', 'Анна Жукова'), ('klimovaf', 'Валентина Климкова'), ('pavlenkoa', 'Анастасия Павленко'), ('slavinskayat', 'Татьяна Славинская'), ('strikovv', 'Владислав Штрыков'), ('shtrikovi', 'Игорь Штрыков'), ('kondratovf', 'Алексей Кондратов'), ('zalubivskiya', 'Алексей Залюбовский'), ('kuznecova', 'Алексей Кузнецов'), ('stringinai', 'Ирина Стрыгина'), ('kolesnika', 'Алина Колесник'), ('savelevv', 'Евгений Савельев'), ('melnichenkon', 'Наталья Мельничук'), ('resep', 'Офис Менеджер'), ('fomine', 'Евгений Фомин')], default=' ', help_text='Необязательно к заполнению', max_length=100, verbose_name='Риелтор в сделке №4'),
        ),
        migrations.AlterField(
            model_name='otchet_nov',
            name='reelt5',
            field=models.CharField(blank=True, choices=[('homka', 'Роман Домников'), ('demo', 'demo demon'), ('surgutskayao', 'Оксана Сургутская'), ('alekseevau', 'Юлия Алексеева'), ('crutihinao', 'Ольга Крутихина'), ('mihailovau', 'Юлия Михайлова'), ('samoryadova', 'Андрей Саморядов'), ('shalimovav', 'Виктория Шалимова'), ('skripkinaa', 'Анастасия Скрипкина'), ('odabashyane', 'Эдуард Одабащьян'), ('rnovikov', 'Роман Новиков'), ('ujashakueva', 'Римма Джашакуева'), ('refremov', 'Руслан Ефремов'), ('aegorova', 'Анжелика Егорова'), ('livina', 'Людмила Ильина'), ('mkaskov', 'Максим Касков'), ('vorinchin', 'Владимир Оринчин'), ('novsyanikova', 'Нина Овсянникова'), ('rpoluvyanov', 'Роман Полувьянов'), ('isolovova', 'Инна Соловьева'), ('nsolovova', 'Наталья Соловьева'), ('paninv', 'Владислав Панин'), ('leontevd', 'Дмитрий Леонтьев'), ('makarovam', 'Марина Макарова'), ('maslovam', 'Марина Маслова'), ('novikove', 'Евгений Новиков'), ('stasukv', 'Вячеслав Стасюк'), ('zabolotiya', 'Алексей Заболотный'), ('liminae', 'Елена Лимина'), ('panasyka', 'Александр Панасюк'), ('tyrins', 'Сергей Тюрин'), ('zabolotiyd', 'Дмитрий Заболотный'), ('ivashenko', 'Алексей Иващенко'), ('jarkovan', 'Наталья Жаркова'), ('kazancevaa', 'Анастасия Казанцева'), ('mihailova', 'Антон Михайлов'), ('panochkin', 'Виктор Паночкин'), ('samodelovao', 'Ольга Самоделова'), ('samodelova', 'Андрей Самоделов'), ('shatskayan', 'Наталья Шацкая'), ('shutenkoa', 'Антон Шутенко'), ('sukhobaevskayam', 'Марина Сухобаевская'), ('timofeevas', 'Светлана Тимофеева'), ('uldasheva', 'Андрей Юлдашев'), ('tretuake', 'Евгений Третяк'), ('stepanovao', 'Ольга Степанова'), ('gukovau', 'Юлия Жукова'), ('maskarao', 'Оксана Машкара'), ('ermolovat', 'Татьяна Ермолова'), ('chelyadinovao', 'Ольга Челядинова'), ('savickayai', 'Ирина Савицкая'), ('milovanovv', 'Виктор Милованов'), ('golovind', 'Дмитрий Головин'), ('rudnevae', 'Елена Руднева'), ('cipurdeyo', 'Олег Ципурдей'), ('yaglova', 'Алексей Яглов'), ('deminaa', 'Анжелика Демина'), ('vishnevskiya', 'Александр Вишневецкий'), ('gukovaa', 'Анна Жукова'), ('klimovaf', 'Валентина Климкова'), ('pavlenkoa', 'Анастасия Павленко'), ('slavinskayat', 'Татьяна Славинская'), ('strikovv', 'Владислав Штрыков'), ('shtrikovi', 'Игорь Штрыков'), ('kondratovf', 'Алексей Кондратов'), ('zalubivskiya', 'Алексей Залюбовский'), ('kuznecova', 'Алексей Кузнецов'), ('stringinai', 'Ирина Стрыгина'), ('kolesnika', 'Алина Колесник'), ('savelevv', 'Евгений Савельев'), ('melnichenkon', 'Наталья Мельничук'), ('resep', 'Офис Менеджер'), ('fomine', 'Евгений Фомин')], default=' ', help_text='Необязательно к заполнению', max_length=100, verbose_name='Риелтор в сделке №5'),
        ),
        migrations.AlterField(
            model_name='otchet_nov',
            name='reelt6',
            field=models.CharField(blank=True, choices=[('homka', 'Роман Домников'), ('demo', 'demo demon'), ('surgutskayao', 'Оксана Сургутская'), ('alekseevau', 'Юлия Алексеева'), ('crutihinao', 'Ольга Крутихина'), ('mihailovau', 'Юлия Михайлова'), ('samoryadova', 'Андрей Саморядов'), ('shalimovav', 'Виктория Шалимова'), ('skripkinaa', 'Анастасия Скрипкина'), ('odabashyane', 'Эдуард Одабащьян'), ('rnovikov', 'Роман Новиков'), ('ujashakueva', 'Римма Джашакуева'), ('refremov', 'Руслан Ефремов'), ('aegorova', 'Анжелика Егорова'), ('livina', 'Людмила Ильина'), ('mkaskov', 'Максим Касков'), ('vorinchin', 'Владимир Оринчин'), ('novsyanikova', 'Нина Овсянникова'), ('rpoluvyanov', 'Роман Полувьянов'), ('isolovova', 'Инна Соловьева'), ('nsolovova', 'Наталья Соловьева'), ('paninv', 'Владислав Панин'), ('leontevd', 'Дмитрий Леонтьев'), ('makarovam', 'Марина Макарова'), ('maslovam', 'Марина Маслова'), ('novikove', 'Евгений Новиков'), ('stasukv', 'Вячеслав Стасюк'), ('zabolotiya', 'Алексей Заболотный'), ('liminae', 'Елена Лимина'), ('panasyka', 'Александр Панасюк'), ('tyrins', 'Сергей Тюрин'), ('zabolotiyd', 'Дмитрий Заболотный'), ('ivashenko', 'Алексей Иващенко'), ('jarkovan', 'Наталья Жаркова'), ('kazancevaa', 'Анастасия Казанцева'), ('mihailova', 'Антон Михайлов'), ('panochkin', 'Виктор Паночкин'), ('samodelovao', 'Ольга Самоделова'), ('samodelova', 'Андрей Самоделов'), ('shatskayan', 'Наталья Шацкая'), ('shutenkoa', 'Антон Шутенко'), ('sukhobaevskayam', 'Марина Сухобаевская'), ('timofeevas', 'Светлана Тимофеева'), ('uldasheva', 'Андрей Юлдашев'), ('tretuake', 'Евгений Третяк'), ('stepanovao', 'Ольга Степанова'), ('gukovau', 'Юлия Жукова'), ('maskarao', 'Оксана Машкара'), ('ermolovat', 'Татьяна Ермолова'), ('chelyadinovao', 'Ольга Челядинова'), ('savickayai', 'Ирина Савицкая'), ('milovanovv', 'Виктор Милованов'), ('golovind', 'Дмитрий Головин'), ('rudnevae', 'Елена Руднева'), ('cipurdeyo', 'Олег Ципурдей'), ('yaglova', 'Алексей Яглов'), ('deminaa', 'Анжелика Демина'), ('vishnevskiya', 'Александр Вишневецкий'), ('gukovaa', 'Анна Жукова'), ('klimovaf', 'Валентина Климкова'), ('pavlenkoa', 'Анастасия Павленко'), ('slavinskayat', 'Татьяна Славинская'), ('strikovv', 'Владислав Штрыков'), ('shtrikovi', 'Игорь Штрыков'), ('kondratovf', 'Алексей Кондратов'), ('zalubivskiya', 'Алексей Залюбовский'), ('kuznecova', 'Алексей Кузнецов'), ('stringinai', 'Ирина Стрыгина'), ('kolesnika', 'Алина Колесник'), ('savelevv', 'Евгений Савельев'), ('melnichenkon', 'Наталья Мельничук'), ('resep', 'Офис Менеджер'), ('fomine', 'Евгений Фомин')], default=' ', help_text='Необязательно к заполнению', max_length=100, verbose_name='Риелтор в сделке №6'),
        ),
        migrations.AlterField(
            model_name='otchet_nov',
            name='reelt7',
            field=models.CharField(blank=True, choices=[('homka', 'Роман Домников'), ('demo', 'demo demon'), ('surgutskayao', 'Оксана Сургутская'), ('alekseevau', 'Юлия Алексеева'), ('crutihinao', 'Ольга Крутихина'), ('mihailovau', 'Юлия Михайлова'), ('samoryadova', 'Андрей Саморядов'), ('shalimovav', 'Виктория Шалимова'), ('skripkinaa', 'Анастасия Скрипкина'), ('odabashyane', 'Эдуард Одабащьян'), ('rnovikov', 'Роман Новиков'), ('ujashakueva', 'Римма Джашакуева'), ('refremov', 'Руслан Ефремов'), ('aegorova', 'Анжелика Егорова'), ('livina', 'Людмила Ильина'), ('mkaskov', 'Максим Касков'), ('vorinchin', 'Владимир Оринчин'), ('novsyanikova', 'Нина Овсянникова'), ('rpoluvyanov', 'Роман Полувьянов'), ('isolovova', 'Инна Соловьева'), ('nsolovova', 'Наталья Соловьева'), ('paninv', 'Владислав Панин'), ('leontevd', 'Дмитрий Леонтьев'), ('makarovam', 'Марина Макарова'), ('maslovam', 'Марина Маслова'), ('novikove', 'Евгений Новиков'), ('stasukv', 'Вячеслав Стасюк'), ('zabolotiya', 'Алексей Заболотный'), ('liminae', 'Елена Лимина'), ('panasyka', 'Александр Панасюк'), ('tyrins', 'Сергей Тюрин'), ('zabolotiyd', 'Дмитрий Заболотный'), ('ivashenko', 'Алексей Иващенко'), ('jarkovan', 'Наталья Жаркова'), ('kazancevaa', 'Анастасия Казанцева'), ('mihailova', 'Антон Михайлов'), ('panochkin', 'Виктор Паночкин'), ('samodelovao', 'Ольга Самоделова'), ('samodelova', 'Андрей Самоделов'), ('shatskayan', 'Наталья Шацкая'), ('shutenkoa', 'Антон Шутенко'), ('sukhobaevskayam', 'Марина Сухобаевская'), ('timofeevas', 'Светлана Тимофеева'), ('uldasheva', 'Андрей Юлдашев'), ('tretuake', 'Евгений Третяк'), ('stepanovao', 'Ольга Степанова'), ('gukovau', 'Юлия Жукова'), ('maskarao', 'Оксана Машкара'), ('ermolovat', 'Татьяна Ермолова'), ('chelyadinovao', 'Ольга Челядинова'), ('savickayai', 'Ирина Савицкая'), ('milovanovv', 'Виктор Милованов'), ('golovind', 'Дмитрий Головин'), ('rudnevae', 'Елена Руднева'), ('cipurdeyo', 'Олег Ципурдей'), ('yaglova', 'Алексей Яглов'), ('deminaa', 'Анжелика Демина'), ('vishnevskiya', 'Александр Вишневецкий'), ('gukovaa', 'Анна Жукова'), ('klimovaf', 'Валентина Климкова'), ('pavlenkoa', 'Анастасия Павленко'), ('slavinskayat', 'Татьяна Славинская'), ('strikovv', 'Владислав Штрыков'), ('shtrikovi', 'Игорь Штрыков'), ('kondratovf', 'Алексей Кондратов'), ('zalubivskiya', 'Алексей Залюбовский'), ('kuznecova', 'Алексей Кузнецов'), ('stringinai', 'Ирина Стрыгина'), ('kolesnika', 'Алина Колесник'), ('savelevv', 'Евгений Савельев'), ('melnichenkon', 'Наталья Мельничук'), ('resep', 'Офис Менеджер'), ('fomine', 'Евгений Фомин')], default=' ', help_text='Необязательно к заполнению', max_length=100, verbose_name='Риелтор в сделке №7'),
        ),
        migrations.AlterField(
            model_name='otchet_nov',
            name='reelt8',
            field=models.CharField(blank=True, choices=[('homka', 'Роман Домников'), ('demo', 'demo demon'), ('surgutskayao', 'Оксана Сургутская'), ('alekseevau', 'Юлия Алексеева'), ('crutihinao', 'Ольга Крутихина'), ('mihailovau', 'Юлия Михайлова'), ('samoryadova', 'Андрей Саморядов'), ('shalimovav', 'Виктория Шалимова'), ('skripkinaa', 'Анастасия Скрипкина'), ('odabashyane', 'Эдуард Одабащьян'), ('rnovikov', 'Роман Новиков'), ('ujashakueva', 'Римма Джашакуева'), ('refremov', 'Руслан Ефремов'), ('aegorova', 'Анжелика Егорова'), ('livina', 'Людмила Ильина'), ('mkaskov', 'Максим Касков'), ('vorinchin', 'Владимир Оринчин'), ('novsyanikova', 'Нина Овсянникова'), ('rpoluvyanov', 'Роман Полувьянов'), ('isolovova', 'Инна Соловьева'), ('nsolovova', 'Наталья Соловьева'), ('paninv', 'Владислав Панин'), ('leontevd', 'Дмитрий Леонтьев'), ('makarovam', 'Марина Макарова'), ('maslovam', 'Марина Маслова'), ('novikove', 'Евгений Новиков'), ('stasukv', 'Вячеслав Стасюк'), ('zabolotiya', 'Алексей Заболотный'), ('liminae', 'Елена Лимина'), ('panasyka', 'Александр Панасюк'), ('tyrins', 'Сергей Тюрин'), ('zabolotiyd', 'Дмитрий Заболотный'), ('ivashenko', 'Алексей Иващенко'), ('jarkovan', 'Наталья Жаркова'), ('kazancevaa', 'Анастасия Казанцева'), ('mihailova', 'Антон Михайлов'), ('panochkin', 'Виктор Паночкин'), ('samodelovao', 'Ольга Самоделова'), ('samodelova', 'Андрей Самоделов'), ('shatskayan', 'Наталья Шацкая'), ('shutenkoa', 'Антон Шутенко'), ('sukhobaevskayam', 'Марина Сухобаевская'), ('timofeevas', 'Светлана Тимофеева'), ('uldasheva', 'Андрей Юлдашев'), ('tretuake', 'Евгений Третяк'), ('stepanovao', 'Ольга Степанова'), ('gukovau', 'Юлия Жукова'), ('maskarao', 'Оксана Машкара'), ('ermolovat', 'Татьяна Ермолова'), ('chelyadinovao', 'Ольга Челядинова'), ('savickayai', 'Ирина Савицкая'), ('milovanovv', 'Виктор Милованов'), ('golovind', 'Дмитрий Головин'), ('rudnevae', 'Елена Руднева'), ('cipurdeyo', 'Олег Ципурдей'), ('yaglova', 'Алексей Яглов'), ('deminaa', 'Анжелика Демина'), ('vishnevskiya', 'Александр Вишневецкий'), ('gukovaa', 'Анна Жукова'), ('klimovaf', 'Валентина Климкова'), ('pavlenkoa', 'Анастасия Павленко'), ('slavinskayat', 'Татьяна Славинская'), ('strikovv', 'Владислав Штрыков'), ('shtrikovi', 'Игорь Штрыков'), ('kondratovf', 'Алексей Кондратов'), ('zalubivskiya', 'Алексей Залюбовский'), ('kuznecova', 'Алексей Кузнецов'), ('stringinai', 'Ирина Стрыгина'), ('kolesnika', 'Алина Колесник'), ('savelevv', 'Евгений Савельев'), ('melnichenkon', 'Наталья Мельничук'), ('resep', 'Офис Менеджер'), ('fomine', 'Евгений Фомин')], default=' ', help_text='Необязательно к заполнению', max_length=100, verbose_name='Риелтор в сделке №8'),
        ),
        migrations.AlterField(
            model_name='otchet_nov',
            name='reelt9',
            field=models.CharField(blank=True, choices=[('homka', 'Роман Домников'), ('demo', 'demo demon'), ('surgutskayao', 'Оксана Сургутская'), ('alekseevau', 'Юлия Алексеева'), ('crutihinao', 'Ольга Крутихина'), ('mihailovau', 'Юлия Михайлова'), ('samoryadova', 'Андрей Саморядов'), ('shalimovav', 'Виктория Шалимова'), ('skripkinaa', 'Анастасия Скрипкина'), ('odabashyane', 'Эдуард Одабащьян'), ('rnovikov', 'Роман Новиков'), ('ujashakueva', 'Римма Джашакуева'), ('refremov', 'Руслан Ефремов'), ('aegorova', 'Анжелика Егорова'), ('livina', 'Людмила Ильина'), ('mkaskov', 'Максим Касков'), ('vorinchin', 'Владимир Оринчин'), ('novsyanikova', 'Нина Овсянникова'), ('rpoluvyanov', 'Роман Полувьянов'), ('isolovova', 'Инна Соловьева'), ('nsolovova', 'Наталья Соловьева'), ('paninv', 'Владислав Панин'), ('leontevd', 'Дмитрий Леонтьев'), ('makarovam', 'Марина Макарова'), ('maslovam', 'Марина Маслова'), ('novikove', 'Евгений Новиков'), ('stasukv', 'Вячеслав Стасюк'), ('zabolotiya', 'Алексей Заболотный'), ('liminae', 'Елена Лимина'), ('panasyka', 'Александр Панасюк'), ('tyrins', 'Сергей Тюрин'), ('zabolotiyd', 'Дмитрий Заболотный'), ('ivashenko', 'Алексей Иващенко'), ('jarkovan', 'Наталья Жаркова'), ('kazancevaa', 'Анастасия Казанцева'), ('mihailova', 'Антон Михайлов'), ('panochkin', 'Виктор Паночкин'), ('samodelovao', 'Ольга Самоделова'), ('samodelova', 'Андрей Самоделов'), ('shatskayan', 'Наталья Шацкая'), ('shutenkoa', 'Антон Шутенко'), ('sukhobaevskayam', 'Марина Сухобаевская'), ('timofeevas', 'Светлана Тимофеева'), ('uldasheva', 'Андрей Юлдашев'), ('tretuake', 'Евгений Третяк'), ('stepanovao', 'Ольга Степанова'), ('gukovau', 'Юлия Жукова'), ('maskarao', 'Оксана Машкара'), ('ermolovat', 'Татьяна Ермолова'), ('chelyadinovao', 'Ольга Челядинова'), ('savickayai', 'Ирина Савицкая'), ('milovanovv', 'Виктор Милованов'), ('golovind', 'Дмитрий Головин'), ('rudnevae', 'Елена Руднева'), ('cipurdeyo', 'Олег Ципурдей'), ('yaglova', 'Алексей Яглов'), ('deminaa', 'Анжелика Демина'), ('vishnevskiya', 'Александр Вишневецкий'), ('gukovaa', 'Анна Жукова'), ('klimovaf', 'Валентина Климкова'), ('pavlenkoa', 'Анастасия Павленко'), ('slavinskayat', 'Татьяна Славинская'), ('strikovv', 'Владислав Штрыков'), ('shtrikovi', 'Игорь Штрыков'), ('kondratovf', 'Алексей Кондратов'), ('zalubivskiya', 'Алексей Залюбовский'), ('kuznecova', 'Алексей Кузнецов'), ('stringinai', 'Ирина Стрыгина'), ('kolesnika', 'Алина Колесник'), ('savelevv', 'Евгений Савельев'), ('melnichenkon', 'Наталья Мельничук'), ('resep', 'Офис Менеджер'), ('fomine', 'Евгений Фомин')], default=' ', help_text='Необязательно к заполнению', max_length=100, verbose_name='Риелтор в сделке №9'),
        ),
        migrations.AlterField(
            model_name='zayavka',
            name='date_vzyatia',
            field=models.DateTimeField(auto_now=True, verbose_name='Взято в работу:'),
        ),
    ]
