# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-09-27 12:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0116_auto_20180831_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat_obj',
            name='date_vigr_sait',
            field=models.DateField(verbose_name='Дата выгрузки на сайт:'),
        ),
        migrations.AlterField(
            model_name='otchet_nov',
            name='reelt1',
            field=models.CharField(blank=True, choices=[('zalubovskiya', ' '), ('seo', ' '), ('demo', 'demon demo'), ('alekseevau', 'Алексеева Юлия'), ('belyaevd', 'Беляев Дмитрий'), ('belyaevag', 'Беляева Галина'), ('vinnikovao', 'Винникова Анастасия'), ('vishnevskiya', 'Вишневецкий Александр'), ('gainullini', 'Гайнуллин Иван'), ('golovind', 'Головин Дмитрий'), ('deminaa', 'Демина Анжелика'), ('ujashakueva', 'Джашакуева Римма'), ('dogadinau', 'Догадина Юлия'), ('homka', 'Домников Роман'), ('aegorova', 'Егорова Анжелика'), ('ermolovat', 'Ермолова Татьяна'), ('refremov', 'Ефремов Руслан'), ('jarkovan', 'Жаркова Наталья'), ('gukovg', 'Жуков Григорий'), ('gukovau', 'Жукова Юлия'), ('gukovaa', 'Жукова Анна'), ('zabolotiya', 'Заболотный Алексей'), ('zabolotiyd', 'Заболотный Дмитрий'), ('zagorskaya', 'Загорская Юлия'), ('zaycevaa', 'Зайцева Алина'), ('zalubivskiya', 'Залюбовский Алексей'), ('ibragimoval', 'Ибрагимова Лейсан'), ('ivashenko', 'Иващенко Алексей'), ('ivlevan', 'Иевлева Наталья'), ('livina', 'Ильина Людмила'), ('isagadjievag', 'Исагаджиева Гуля'), ('kazancevaa', 'Казанцева Анастасия'), ('kamornikove', 'Каморников Евгений'), ('mkaskov', 'Касков Максим'), ('klimovaf', 'Климкова Валентина'), ('kozus', 'Козусь Анастасия'), ('kolesnika', 'Колесник Алина'), ('kondratovf', 'Кондратов Алексей'), ('konoshece', 'Коношец Елена'), ('crutihinao', 'Крутихина Ольга'), ('kudryavcevao', 'Кудряшова Оксана'), ('kudryashovae', 'Кудряшова Елена'), ('kuznecova', 'Кузнецов Алексей'), ('leontevd', 'Леонтьев Дмитрий'), ('liminae', 'Лимина Елена'), ('lobjanidzev', 'Лобжанидзе Владимир'), ('luganovav', 'Луганова Виктория'), ('makarovam', 'Макарова Марина'), ('maslovam', 'Маслова Марина'), ('maskarao', 'Машкара Оксана'), ('melnichenkon', 'Мельничук Наталья'), ('resep', 'Менеджер Офис'), ('meshkovn', 'Мешков Николай'), ('milovanovv', 'Милованов Виктор'), ('miroshnichenkoi', 'Мирошниченко Ирина'), ('misarovak', 'Мисарова Кристина'), ('mitte', 'Митт Елена'), ('mihailova', 'Михайлов Антон'), ('mihailovau', 'Михайлова Юлия'), ('musaevm', 'Мусаев Мухтар'), ('rnovikov', 'Новиков Роман'), ('novikove', 'Новиков Евгений'), ('novsyanikova', 'Овсянникова Нина'), ('odabashyane', 'Одабащьян Эдуард'), ('vorinchin', 'Оринчин Владимир'), ('aresep', 'Офис Менеджер Адлер'), ('pavlenkoa', 'Павленко Анастасия'), ('panasyka', 'Панасюк Александр'), ('paninv', 'Панин Владислав'), ('perestoroninav', 'Пересторонина Виктория'), ('rpoluvyanov', 'Полувьянов Роман'), ('rudnevae', 'Руднева Елена'), ('savelevv', 'Савельев Евгений'), ('samodelova', 'Самоделов Андрей'), ('samodelovao', 'Самоделова Ольга'), ('samoryadova', 'Саморядов Андрей'), ('seliverstovav', 'Селиверстова Виктория'), ('skripkinaa', 'Скрипкина Анастасия'), ('slavinskayat', 'Славинская Татьяна'), ('slukinam', 'Слукина Марина'), ('isolovova', 'Соловьева Инна'), ('nsolovova', 'Соловьева Наталья'), ('stasukv', 'Стасюк Вячеслав'), ('stepanovao', 'Степанова Ольга'), ('strahovi', 'Страхов Илья'), ('stringinai', 'Стрыгина Ирина'), ('surgutskayao', 'Сургутская Оксана'), ('taskinaa', 'Таскина Анастасия'), ('tretuake', 'Третяк Евгений'), ('tyrins', 'Тюрин Сергей'), ('ushakova', 'Ушаков Антон'), ('fedoseevan', 'Федосеева Надежда'), ('fomine', 'Фомин Евгений'), ('cipurdeyo', 'Ципурдей Олег'), ('cherencovv', 'Черенков '), ('chimbarovv', 'Чимбаров Владимир'), ('shalimovav', 'Шалимова Виктория'), ('shatskayan', 'Шацкая Наталья'), ('strikovv', 'Штрыков Владислав'), ('shtrikovi', 'Штрыков Игорь'), ('shugarinae', 'Шурыгина Елена'), ('yaglova', 'Яглов Алексей')], default=' ', help_text='Обязательно к заполнению!', max_length=100, verbose_name='Риелтор в сделке №1'),
        ),
        migrations.AlterField(
            model_name='otchet_nov',
            name='reelt10',
            field=models.CharField(blank=True, choices=[('zalubovskiya', ' '), ('seo', ' '), ('demo', 'demon demo'), ('alekseevau', 'Алексеева Юлия'), ('belyaevd', 'Беляев Дмитрий'), ('belyaevag', 'Беляева Галина'), ('vinnikovao', 'Винникова Анастасия'), ('vishnevskiya', 'Вишневецкий Александр'), ('gainullini', 'Гайнуллин Иван'), ('golovind', 'Головин Дмитрий'), ('deminaa', 'Демина Анжелика'), ('ujashakueva', 'Джашакуева Римма'), ('dogadinau', 'Догадина Юлия'), ('homka', 'Домников Роман'), ('aegorova', 'Егорова Анжелика'), ('ermolovat', 'Ермолова Татьяна'), ('refremov', 'Ефремов Руслан'), ('jarkovan', 'Жаркова Наталья'), ('gukovg', 'Жуков Григорий'), ('gukovau', 'Жукова Юлия'), ('gukovaa', 'Жукова Анна'), ('zabolotiya', 'Заболотный Алексей'), ('zabolotiyd', 'Заболотный Дмитрий'), ('zagorskaya', 'Загорская Юлия'), ('zaycevaa', 'Зайцева Алина'), ('zalubivskiya', 'Залюбовский Алексей'), ('ibragimoval', 'Ибрагимова Лейсан'), ('ivashenko', 'Иващенко Алексей'), ('ivlevan', 'Иевлева Наталья'), ('livina', 'Ильина Людмила'), ('isagadjievag', 'Исагаджиева Гуля'), ('kazancevaa', 'Казанцева Анастасия'), ('kamornikove', 'Каморников Евгений'), ('mkaskov', 'Касков Максим'), ('klimovaf', 'Климкова Валентина'), ('kozus', 'Козусь Анастасия'), ('kolesnika', 'Колесник Алина'), ('kondratovf', 'Кондратов Алексей'), ('konoshece', 'Коношец Елена'), ('crutihinao', 'Крутихина Ольга'), ('kudryavcevao', 'Кудряшова Оксана'), ('kudryashovae', 'Кудряшова Елена'), ('kuznecova', 'Кузнецов Алексей'), ('leontevd', 'Леонтьев Дмитрий'), ('liminae', 'Лимина Елена'), ('lobjanidzev', 'Лобжанидзе Владимир'), ('luganovav', 'Луганова Виктория'), ('makarovam', 'Макарова Марина'), ('maslovam', 'Маслова Марина'), ('maskarao', 'Машкара Оксана'), ('melnichenkon', 'Мельничук Наталья'), ('resep', 'Менеджер Офис'), ('meshkovn', 'Мешков Николай'), ('milovanovv', 'Милованов Виктор'), ('miroshnichenkoi', 'Мирошниченко Ирина'), ('misarovak', 'Мисарова Кристина'), ('mitte', 'Митт Елена'), ('mihailova', 'Михайлов Антон'), ('mihailovau', 'Михайлова Юлия'), ('musaevm', 'Мусаев Мухтар'), ('rnovikov', 'Новиков Роман'), ('novikove', 'Новиков Евгений'), ('novsyanikova', 'Овсянникова Нина'), ('odabashyane', 'Одабащьян Эдуард'), ('vorinchin', 'Оринчин Владимир'), ('aresep', 'Офис Менеджер Адлер'), ('pavlenkoa', 'Павленко Анастасия'), ('panasyka', 'Панасюк Александр'), ('paninv', 'Панин Владислав'), ('perestoroninav', 'Пересторонина Виктория'), ('rpoluvyanov', 'Полувьянов Роман'), ('rudnevae', 'Руднева Елена'), ('savelevv', 'Савельев Евгений'), ('samodelova', 'Самоделов Андрей'), ('samodelovao', 'Самоделова Ольга'), ('samoryadova', 'Саморядов Андрей'), ('seliverstovav', 'Селиверстова Виктория'), ('skripkinaa', 'Скрипкина Анастасия'), ('slavinskayat', 'Славинская Татьяна'), ('slukinam', 'Слукина Марина'), ('isolovova', 'Соловьева Инна'), ('nsolovova', 'Соловьева Наталья'), ('stasukv', 'Стасюк Вячеслав'), ('stepanovao', 'Степанова Ольга'), ('strahovi', 'Страхов Илья'), ('stringinai', 'Стрыгина Ирина'), ('surgutskayao', 'Сургутская Оксана'), ('taskinaa', 'Таскина Анастасия'), ('tretuake', 'Третяк Евгений'), ('tyrins', 'Тюрин Сергей'), ('ushakova', 'Ушаков Антон'), ('fedoseevan', 'Федосеева Надежда'), ('fomine', 'Фомин Евгений'), ('cipurdeyo', 'Ципурдей Олег'), ('cherencovv', 'Черенков '), ('chimbarovv', 'Чимбаров Владимир'), ('shalimovav', 'Шалимова Виктория'), ('shatskayan', 'Шацкая Наталья'), ('strikovv', 'Штрыков Владислав'), ('shtrikovi', 'Штрыков Игорь'), ('shugarinae', 'Шурыгина Елена'), ('yaglova', 'Яглов Алексей')], default=' ', help_text='Необязательно к заполнению', max_length=100, verbose_name='Риелтор в сделке №10'),
        ),
        migrations.AlterField(
            model_name='otchet_nov',
            name='reelt2',
            field=models.CharField(blank=True, choices=[('zalubovskiya', ' '), ('seo', ' '), ('demo', 'demon demo'), ('alekseevau', 'Алексеева Юлия'), ('belyaevd', 'Беляев Дмитрий'), ('belyaevag', 'Беляева Галина'), ('vinnikovao', 'Винникова Анастасия'), ('vishnevskiya', 'Вишневецкий Александр'), ('gainullini', 'Гайнуллин Иван'), ('golovind', 'Головин Дмитрий'), ('deminaa', 'Демина Анжелика'), ('ujashakueva', 'Джашакуева Римма'), ('dogadinau', 'Догадина Юлия'), ('homka', 'Домников Роман'), ('aegorova', 'Егорова Анжелика'), ('ermolovat', 'Ермолова Татьяна'), ('refremov', 'Ефремов Руслан'), ('jarkovan', 'Жаркова Наталья'), ('gukovg', 'Жуков Григорий'), ('gukovau', 'Жукова Юлия'), ('gukovaa', 'Жукова Анна'), ('zabolotiya', 'Заболотный Алексей'), ('zabolotiyd', 'Заболотный Дмитрий'), ('zagorskaya', 'Загорская Юлия'), ('zaycevaa', 'Зайцева Алина'), ('zalubivskiya', 'Залюбовский Алексей'), ('ibragimoval', 'Ибрагимова Лейсан'), ('ivashenko', 'Иващенко Алексей'), ('ivlevan', 'Иевлева Наталья'), ('livina', 'Ильина Людмила'), ('isagadjievag', 'Исагаджиева Гуля'), ('kazancevaa', 'Казанцева Анастасия'), ('kamornikove', 'Каморников Евгений'), ('mkaskov', 'Касков Максим'), ('klimovaf', 'Климкова Валентина'), ('kozus', 'Козусь Анастасия'), ('kolesnika', 'Колесник Алина'), ('kondratovf', 'Кондратов Алексей'), ('konoshece', 'Коношец Елена'), ('crutihinao', 'Крутихина Ольга'), ('kudryavcevao', 'Кудряшова Оксана'), ('kudryashovae', 'Кудряшова Елена'), ('kuznecova', 'Кузнецов Алексей'), ('leontevd', 'Леонтьев Дмитрий'), ('liminae', 'Лимина Елена'), ('lobjanidzev', 'Лобжанидзе Владимир'), ('luganovav', 'Луганова Виктория'), ('makarovam', 'Макарова Марина'), ('maslovam', 'Маслова Марина'), ('maskarao', 'Машкара Оксана'), ('melnichenkon', 'Мельничук Наталья'), ('resep', 'Менеджер Офис'), ('meshkovn', 'Мешков Николай'), ('milovanovv', 'Милованов Виктор'), ('miroshnichenkoi', 'Мирошниченко Ирина'), ('misarovak', 'Мисарова Кристина'), ('mitte', 'Митт Елена'), ('mihailova', 'Михайлов Антон'), ('mihailovau', 'Михайлова Юлия'), ('musaevm', 'Мусаев Мухтар'), ('rnovikov', 'Новиков Роман'), ('novikove', 'Новиков Евгений'), ('novsyanikova', 'Овсянникова Нина'), ('odabashyane', 'Одабащьян Эдуард'), ('vorinchin', 'Оринчин Владимир'), ('aresep', 'Офис Менеджер Адлер'), ('pavlenkoa', 'Павленко Анастасия'), ('panasyka', 'Панасюк Александр'), ('paninv', 'Панин Владислав'), ('perestoroninav', 'Пересторонина Виктория'), ('rpoluvyanov', 'Полувьянов Роман'), ('rudnevae', 'Руднева Елена'), ('savelevv', 'Савельев Евгений'), ('samodelova', 'Самоделов Андрей'), ('samodelovao', 'Самоделова Ольга'), ('samoryadova', 'Саморядов Андрей'), ('seliverstovav', 'Селиверстова Виктория'), ('skripkinaa', 'Скрипкина Анастасия'), ('slavinskayat', 'Славинская Татьяна'), ('slukinam', 'Слукина Марина'), ('isolovova', 'Соловьева Инна'), ('nsolovova', 'Соловьева Наталья'), ('stasukv', 'Стасюк Вячеслав'), ('stepanovao', 'Степанова Ольга'), ('strahovi', 'Страхов Илья'), ('stringinai', 'Стрыгина Ирина'), ('surgutskayao', 'Сургутская Оксана'), ('taskinaa', 'Таскина Анастасия'), ('tretuake', 'Третяк Евгений'), ('tyrins', 'Тюрин Сергей'), ('ushakova', 'Ушаков Антон'), ('fedoseevan', 'Федосеева Надежда'), ('fomine', 'Фомин Евгений'), ('cipurdeyo', 'Ципурдей Олег'), ('cherencovv', 'Черенков '), ('chimbarovv', 'Чимбаров Владимир'), ('shalimovav', 'Шалимова Виктория'), ('shatskayan', 'Шацкая Наталья'), ('strikovv', 'Штрыков Владислав'), ('shtrikovi', 'Штрыков Игорь'), ('shugarinae', 'Шурыгина Елена'), ('yaglova', 'Яглов Алексей')], default=' ', help_text='Необязательно к заполнению', max_length=100, verbose_name='Риелтор в сделке №2'),
        ),
        migrations.AlterField(
            model_name='otchet_nov',
            name='reelt3',
            field=models.CharField(blank=True, choices=[('zalubovskiya', ' '), ('seo', ' '), ('demo', 'demon demo'), ('alekseevau', 'Алексеева Юлия'), ('belyaevd', 'Беляев Дмитрий'), ('belyaevag', 'Беляева Галина'), ('vinnikovao', 'Винникова Анастасия'), ('vishnevskiya', 'Вишневецкий Александр'), ('gainullini', 'Гайнуллин Иван'), ('golovind', 'Головин Дмитрий'), ('deminaa', 'Демина Анжелика'), ('ujashakueva', 'Джашакуева Римма'), ('dogadinau', 'Догадина Юлия'), ('homka', 'Домников Роман'), ('aegorova', 'Егорова Анжелика'), ('ermolovat', 'Ермолова Татьяна'), ('refremov', 'Ефремов Руслан'), ('jarkovan', 'Жаркова Наталья'), ('gukovg', 'Жуков Григорий'), ('gukovau', 'Жукова Юлия'), ('gukovaa', 'Жукова Анна'), ('zabolotiya', 'Заболотный Алексей'), ('zabolotiyd', 'Заболотный Дмитрий'), ('zagorskaya', 'Загорская Юлия'), ('zaycevaa', 'Зайцева Алина'), ('zalubivskiya', 'Залюбовский Алексей'), ('ibragimoval', 'Ибрагимова Лейсан'), ('ivashenko', 'Иващенко Алексей'), ('ivlevan', 'Иевлева Наталья'), ('livina', 'Ильина Людмила'), ('isagadjievag', 'Исагаджиева Гуля'), ('kazancevaa', 'Казанцева Анастасия'), ('kamornikove', 'Каморников Евгений'), ('mkaskov', 'Касков Максим'), ('klimovaf', 'Климкова Валентина'), ('kozus', 'Козусь Анастасия'), ('kolesnika', 'Колесник Алина'), ('kondratovf', 'Кондратов Алексей'), ('konoshece', 'Коношец Елена'), ('crutihinao', 'Крутихина Ольга'), ('kudryavcevao', 'Кудряшова Оксана'), ('kudryashovae', 'Кудряшова Елена'), ('kuznecova', 'Кузнецов Алексей'), ('leontevd', 'Леонтьев Дмитрий'), ('liminae', 'Лимина Елена'), ('lobjanidzev', 'Лобжанидзе Владимир'), ('luganovav', 'Луганова Виктория'), ('makarovam', 'Макарова Марина'), ('maslovam', 'Маслова Марина'), ('maskarao', 'Машкара Оксана'), ('melnichenkon', 'Мельничук Наталья'), ('resep', 'Менеджер Офис'), ('meshkovn', 'Мешков Николай'), ('milovanovv', 'Милованов Виктор'), ('miroshnichenkoi', 'Мирошниченко Ирина'), ('misarovak', 'Мисарова Кристина'), ('mitte', 'Митт Елена'), ('mihailova', 'Михайлов Антон'), ('mihailovau', 'Михайлова Юлия'), ('musaevm', 'Мусаев Мухтар'), ('rnovikov', 'Новиков Роман'), ('novikove', 'Новиков Евгений'), ('novsyanikova', 'Овсянникова Нина'), ('odabashyane', 'Одабащьян Эдуард'), ('vorinchin', 'Оринчин Владимир'), ('aresep', 'Офис Менеджер Адлер'), ('pavlenkoa', 'Павленко Анастасия'), ('panasyka', 'Панасюк Александр'), ('paninv', 'Панин Владислав'), ('perestoroninav', 'Пересторонина Виктория'), ('rpoluvyanov', 'Полувьянов Роман'), ('rudnevae', 'Руднева Елена'), ('savelevv', 'Савельев Евгений'), ('samodelova', 'Самоделов Андрей'), ('samodelovao', 'Самоделова Ольга'), ('samoryadova', 'Саморядов Андрей'), ('seliverstovav', 'Селиверстова Виктория'), ('skripkinaa', 'Скрипкина Анастасия'), ('slavinskayat', 'Славинская Татьяна'), ('slukinam', 'Слукина Марина'), ('isolovova', 'Соловьева Инна'), ('nsolovova', 'Соловьева Наталья'), ('stasukv', 'Стасюк Вячеслав'), ('stepanovao', 'Степанова Ольга'), ('strahovi', 'Страхов Илья'), ('stringinai', 'Стрыгина Ирина'), ('surgutskayao', 'Сургутская Оксана'), ('taskinaa', 'Таскина Анастасия'), ('tretuake', 'Третяк Евгений'), ('tyrins', 'Тюрин Сергей'), ('ushakova', 'Ушаков Антон'), ('fedoseevan', 'Федосеева Надежда'), ('fomine', 'Фомин Евгений'), ('cipurdeyo', 'Ципурдей Олег'), ('cherencovv', 'Черенков '), ('chimbarovv', 'Чимбаров Владимир'), ('shalimovav', 'Шалимова Виктория'), ('shatskayan', 'Шацкая Наталья'), ('strikovv', 'Штрыков Владислав'), ('shtrikovi', 'Штрыков Игорь'), ('shugarinae', 'Шурыгина Елена'), ('yaglova', 'Яглов Алексей')], default=' ', help_text='Необязательно к заполнению', max_length=100, verbose_name='Риелтор в сделке №3'),
        ),
        migrations.AlterField(
            model_name='otchet_nov',
            name='reelt4',
            field=models.CharField(blank=True, choices=[('zalubovskiya', ' '), ('seo', ' '), ('demo', 'demon demo'), ('alekseevau', 'Алексеева Юлия'), ('belyaevd', 'Беляев Дмитрий'), ('belyaevag', 'Беляева Галина'), ('vinnikovao', 'Винникова Анастасия'), ('vishnevskiya', 'Вишневецкий Александр'), ('gainullini', 'Гайнуллин Иван'), ('golovind', 'Головин Дмитрий'), ('deminaa', 'Демина Анжелика'), ('ujashakueva', 'Джашакуева Римма'), ('dogadinau', 'Догадина Юлия'), ('homka', 'Домников Роман'), ('aegorova', 'Егорова Анжелика'), ('ermolovat', 'Ермолова Татьяна'), ('refremov', 'Ефремов Руслан'), ('jarkovan', 'Жаркова Наталья'), ('gukovg', 'Жуков Григорий'), ('gukovau', 'Жукова Юлия'), ('gukovaa', 'Жукова Анна'), ('zabolotiya', 'Заболотный Алексей'), ('zabolotiyd', 'Заболотный Дмитрий'), ('zagorskaya', 'Загорская Юлия'), ('zaycevaa', 'Зайцева Алина'), ('zalubivskiya', 'Залюбовский Алексей'), ('ibragimoval', 'Ибрагимова Лейсан'), ('ivashenko', 'Иващенко Алексей'), ('ivlevan', 'Иевлева Наталья'), ('livina', 'Ильина Людмила'), ('isagadjievag', 'Исагаджиева Гуля'), ('kazancevaa', 'Казанцева Анастасия'), ('kamornikove', 'Каморников Евгений'), ('mkaskov', 'Касков Максим'), ('klimovaf', 'Климкова Валентина'), ('kozus', 'Козусь Анастасия'), ('kolesnika', 'Колесник Алина'), ('kondratovf', 'Кондратов Алексей'), ('konoshece', 'Коношец Елена'), ('crutihinao', 'Крутихина Ольга'), ('kudryavcevao', 'Кудряшова Оксана'), ('kudryashovae', 'Кудряшова Елена'), ('kuznecova', 'Кузнецов Алексей'), ('leontevd', 'Леонтьев Дмитрий'), ('liminae', 'Лимина Елена'), ('lobjanidzev', 'Лобжанидзе Владимир'), ('luganovav', 'Луганова Виктория'), ('makarovam', 'Макарова Марина'), ('maslovam', 'Маслова Марина'), ('maskarao', 'Машкара Оксана'), ('melnichenkon', 'Мельничук Наталья'), ('resep', 'Менеджер Офис'), ('meshkovn', 'Мешков Николай'), ('milovanovv', 'Милованов Виктор'), ('miroshnichenkoi', 'Мирошниченко Ирина'), ('misarovak', 'Мисарова Кристина'), ('mitte', 'Митт Елена'), ('mihailova', 'Михайлов Антон'), ('mihailovau', 'Михайлова Юлия'), ('musaevm', 'Мусаев Мухтар'), ('rnovikov', 'Новиков Роман'), ('novikove', 'Новиков Евгений'), ('novsyanikova', 'Овсянникова Нина'), ('odabashyane', 'Одабащьян Эдуард'), ('vorinchin', 'Оринчин Владимир'), ('aresep', 'Офис Менеджер Адлер'), ('pavlenkoa', 'Павленко Анастасия'), ('panasyka', 'Панасюк Александр'), ('paninv', 'Панин Владислав'), ('perestoroninav', 'Пересторонина Виктория'), ('rpoluvyanov', 'Полувьянов Роман'), ('rudnevae', 'Руднева Елена'), ('savelevv', 'Савельев Евгений'), ('samodelova', 'Самоделов Андрей'), ('samodelovao', 'Самоделова Ольга'), ('samoryadova', 'Саморядов Андрей'), ('seliverstovav', 'Селиверстова Виктория'), ('skripkinaa', 'Скрипкина Анастасия'), ('slavinskayat', 'Славинская Татьяна'), ('slukinam', 'Слукина Марина'), ('isolovova', 'Соловьева Инна'), ('nsolovova', 'Соловьева Наталья'), ('stasukv', 'Стасюк Вячеслав'), ('stepanovao', 'Степанова Ольга'), ('strahovi', 'Страхов Илья'), ('stringinai', 'Стрыгина Ирина'), ('surgutskayao', 'Сургутская Оксана'), ('taskinaa', 'Таскина Анастасия'), ('tretuake', 'Третяк Евгений'), ('tyrins', 'Тюрин Сергей'), ('ushakova', 'Ушаков Антон'), ('fedoseevan', 'Федосеева Надежда'), ('fomine', 'Фомин Евгений'), ('cipurdeyo', 'Ципурдей Олег'), ('cherencovv', 'Черенков '), ('chimbarovv', 'Чимбаров Владимир'), ('shalimovav', 'Шалимова Виктория'), ('shatskayan', 'Шацкая Наталья'), ('strikovv', 'Штрыков Владислав'), ('shtrikovi', 'Штрыков Игорь'), ('shugarinae', 'Шурыгина Елена'), ('yaglova', 'Яглов Алексей')], default=' ', help_text='Необязательно к заполнению', max_length=100, verbose_name='Риелтор в сделке №4'),
        ),
        migrations.AlterField(
            model_name='otchet_nov',
            name='reelt5',
            field=models.CharField(blank=True, choices=[('zalubovskiya', ' '), ('seo', ' '), ('demo', 'demon demo'), ('alekseevau', 'Алексеева Юлия'), ('belyaevd', 'Беляев Дмитрий'), ('belyaevag', 'Беляева Галина'), ('vinnikovao', 'Винникова Анастасия'), ('vishnevskiya', 'Вишневецкий Александр'), ('gainullini', 'Гайнуллин Иван'), ('golovind', 'Головин Дмитрий'), ('deminaa', 'Демина Анжелика'), ('ujashakueva', 'Джашакуева Римма'), ('dogadinau', 'Догадина Юлия'), ('homka', 'Домников Роман'), ('aegorova', 'Егорова Анжелика'), ('ermolovat', 'Ермолова Татьяна'), ('refremov', 'Ефремов Руслан'), ('jarkovan', 'Жаркова Наталья'), ('gukovg', 'Жуков Григорий'), ('gukovau', 'Жукова Юлия'), ('gukovaa', 'Жукова Анна'), ('zabolotiya', 'Заболотный Алексей'), ('zabolotiyd', 'Заболотный Дмитрий'), ('zagorskaya', 'Загорская Юлия'), ('zaycevaa', 'Зайцева Алина'), ('zalubivskiya', 'Залюбовский Алексей'), ('ibragimoval', 'Ибрагимова Лейсан'), ('ivashenko', 'Иващенко Алексей'), ('ivlevan', 'Иевлева Наталья'), ('livina', 'Ильина Людмила'), ('isagadjievag', 'Исагаджиева Гуля'), ('kazancevaa', 'Казанцева Анастасия'), ('kamornikove', 'Каморников Евгений'), ('mkaskov', 'Касков Максим'), ('klimovaf', 'Климкова Валентина'), ('kozus', 'Козусь Анастасия'), ('kolesnika', 'Колесник Алина'), ('kondratovf', 'Кондратов Алексей'), ('konoshece', 'Коношец Елена'), ('crutihinao', 'Крутихина Ольга'), ('kudryavcevao', 'Кудряшова Оксана'), ('kudryashovae', 'Кудряшова Елена'), ('kuznecova', 'Кузнецов Алексей'), ('leontevd', 'Леонтьев Дмитрий'), ('liminae', 'Лимина Елена'), ('lobjanidzev', 'Лобжанидзе Владимир'), ('luganovav', 'Луганова Виктория'), ('makarovam', 'Макарова Марина'), ('maslovam', 'Маслова Марина'), ('maskarao', 'Машкара Оксана'), ('melnichenkon', 'Мельничук Наталья'), ('resep', 'Менеджер Офис'), ('meshkovn', 'Мешков Николай'), ('milovanovv', 'Милованов Виктор'), ('miroshnichenkoi', 'Мирошниченко Ирина'), ('misarovak', 'Мисарова Кристина'), ('mitte', 'Митт Елена'), ('mihailova', 'Михайлов Антон'), ('mihailovau', 'Михайлова Юлия'), ('musaevm', 'Мусаев Мухтар'), ('rnovikov', 'Новиков Роман'), ('novikove', 'Новиков Евгений'), ('novsyanikova', 'Овсянникова Нина'), ('odabashyane', 'Одабащьян Эдуард'), ('vorinchin', 'Оринчин Владимир'), ('aresep', 'Офис Менеджер Адлер'), ('pavlenkoa', 'Павленко Анастасия'), ('panasyka', 'Панасюк Александр'), ('paninv', 'Панин Владислав'), ('perestoroninav', 'Пересторонина Виктория'), ('rpoluvyanov', 'Полувьянов Роман'), ('rudnevae', 'Руднева Елена'), ('savelevv', 'Савельев Евгений'), ('samodelova', 'Самоделов Андрей'), ('samodelovao', 'Самоделова Ольга'), ('samoryadova', 'Саморядов Андрей'), ('seliverstovav', 'Селиверстова Виктория'), ('skripkinaa', 'Скрипкина Анастасия'), ('slavinskayat', 'Славинская Татьяна'), ('slukinam', 'Слукина Марина'), ('isolovova', 'Соловьева Инна'), ('nsolovova', 'Соловьева Наталья'), ('stasukv', 'Стасюк Вячеслав'), ('stepanovao', 'Степанова Ольга'), ('strahovi', 'Страхов Илья'), ('stringinai', 'Стрыгина Ирина'), ('surgutskayao', 'Сургутская Оксана'), ('taskinaa', 'Таскина Анастасия'), ('tretuake', 'Третяк Евгений'), ('tyrins', 'Тюрин Сергей'), ('ushakova', 'Ушаков Антон'), ('fedoseevan', 'Федосеева Надежда'), ('fomine', 'Фомин Евгений'), ('cipurdeyo', 'Ципурдей Олег'), ('cherencovv', 'Черенков '), ('chimbarovv', 'Чимбаров Владимир'), ('shalimovav', 'Шалимова Виктория'), ('shatskayan', 'Шацкая Наталья'), ('strikovv', 'Штрыков Владислав'), ('shtrikovi', 'Штрыков Игорь'), ('shugarinae', 'Шурыгина Елена'), ('yaglova', 'Яглов Алексей')], default=' ', help_text='Необязательно к заполнению', max_length=100, verbose_name='Риелтор в сделке №5'),
        ),
        migrations.AlterField(
            model_name='otchet_nov',
            name='reelt6',
            field=models.CharField(blank=True, choices=[('zalubovskiya', ' '), ('seo', ' '), ('demo', 'demon demo'), ('alekseevau', 'Алексеева Юлия'), ('belyaevd', 'Беляев Дмитрий'), ('belyaevag', 'Беляева Галина'), ('vinnikovao', 'Винникова Анастасия'), ('vishnevskiya', 'Вишневецкий Александр'), ('gainullini', 'Гайнуллин Иван'), ('golovind', 'Головин Дмитрий'), ('deminaa', 'Демина Анжелика'), ('ujashakueva', 'Джашакуева Римма'), ('dogadinau', 'Догадина Юлия'), ('homka', 'Домников Роман'), ('aegorova', 'Егорова Анжелика'), ('ermolovat', 'Ермолова Татьяна'), ('refremov', 'Ефремов Руслан'), ('jarkovan', 'Жаркова Наталья'), ('gukovg', 'Жуков Григорий'), ('gukovau', 'Жукова Юлия'), ('gukovaa', 'Жукова Анна'), ('zabolotiya', 'Заболотный Алексей'), ('zabolotiyd', 'Заболотный Дмитрий'), ('zagorskaya', 'Загорская Юлия'), ('zaycevaa', 'Зайцева Алина'), ('zalubivskiya', 'Залюбовский Алексей'), ('ibragimoval', 'Ибрагимова Лейсан'), ('ivashenko', 'Иващенко Алексей'), ('ivlevan', 'Иевлева Наталья'), ('livina', 'Ильина Людмила'), ('isagadjievag', 'Исагаджиева Гуля'), ('kazancevaa', 'Казанцева Анастасия'), ('kamornikove', 'Каморников Евгений'), ('mkaskov', 'Касков Максим'), ('klimovaf', 'Климкова Валентина'), ('kozus', 'Козусь Анастасия'), ('kolesnika', 'Колесник Алина'), ('kondratovf', 'Кондратов Алексей'), ('konoshece', 'Коношец Елена'), ('crutihinao', 'Крутихина Ольга'), ('kudryavcevao', 'Кудряшова Оксана'), ('kudryashovae', 'Кудряшова Елена'), ('kuznecova', 'Кузнецов Алексей'), ('leontevd', 'Леонтьев Дмитрий'), ('liminae', 'Лимина Елена'), ('lobjanidzev', 'Лобжанидзе Владимир'), ('luganovav', 'Луганова Виктория'), ('makarovam', 'Макарова Марина'), ('maslovam', 'Маслова Марина'), ('maskarao', 'Машкара Оксана'), ('melnichenkon', 'Мельничук Наталья'), ('resep', 'Менеджер Офис'), ('meshkovn', 'Мешков Николай'), ('milovanovv', 'Милованов Виктор'), ('miroshnichenkoi', 'Мирошниченко Ирина'), ('misarovak', 'Мисарова Кристина'), ('mitte', 'Митт Елена'), ('mihailova', 'Михайлов Антон'), ('mihailovau', 'Михайлова Юлия'), ('musaevm', 'Мусаев Мухтар'), ('rnovikov', 'Новиков Роман'), ('novikove', 'Новиков Евгений'), ('novsyanikova', 'Овсянникова Нина'), ('odabashyane', 'Одабащьян Эдуард'), ('vorinchin', 'Оринчин Владимир'), ('aresep', 'Офис Менеджер Адлер'), ('pavlenkoa', 'Павленко Анастасия'), ('panasyka', 'Панасюк Александр'), ('paninv', 'Панин Владислав'), ('perestoroninav', 'Пересторонина Виктория'), ('rpoluvyanov', 'Полувьянов Роман'), ('rudnevae', 'Руднева Елена'), ('savelevv', 'Савельев Евгений'), ('samodelova', 'Самоделов Андрей'), ('samodelovao', 'Самоделова Ольга'), ('samoryadova', 'Саморядов Андрей'), ('seliverstovav', 'Селиверстова Виктория'), ('skripkinaa', 'Скрипкина Анастасия'), ('slavinskayat', 'Славинская Татьяна'), ('slukinam', 'Слукина Марина'), ('isolovova', 'Соловьева Инна'), ('nsolovova', 'Соловьева Наталья'), ('stasukv', 'Стасюк Вячеслав'), ('stepanovao', 'Степанова Ольга'), ('strahovi', 'Страхов Илья'), ('stringinai', 'Стрыгина Ирина'), ('surgutskayao', 'Сургутская Оксана'), ('taskinaa', 'Таскина Анастасия'), ('tretuake', 'Третяк Евгений'), ('tyrins', 'Тюрин Сергей'), ('ushakova', 'Ушаков Антон'), ('fedoseevan', 'Федосеева Надежда'), ('fomine', 'Фомин Евгений'), ('cipurdeyo', 'Ципурдей Олег'), ('cherencovv', 'Черенков '), ('chimbarovv', 'Чимбаров Владимир'), ('shalimovav', 'Шалимова Виктория'), ('shatskayan', 'Шацкая Наталья'), ('strikovv', 'Штрыков Владислав'), ('shtrikovi', 'Штрыков Игорь'), ('shugarinae', 'Шурыгина Елена'), ('yaglova', 'Яглов Алексей')], default=' ', help_text='Необязательно к заполнению', max_length=100, verbose_name='Риелтор в сделке №6'),
        ),
        migrations.AlterField(
            model_name='otchet_nov',
            name='reelt7',
            field=models.CharField(blank=True, choices=[('zalubovskiya', ' '), ('seo', ' '), ('demo', 'demon demo'), ('alekseevau', 'Алексеева Юлия'), ('belyaevd', 'Беляев Дмитрий'), ('belyaevag', 'Беляева Галина'), ('vinnikovao', 'Винникова Анастасия'), ('vishnevskiya', 'Вишневецкий Александр'), ('gainullini', 'Гайнуллин Иван'), ('golovind', 'Головин Дмитрий'), ('deminaa', 'Демина Анжелика'), ('ujashakueva', 'Джашакуева Римма'), ('dogadinau', 'Догадина Юлия'), ('homka', 'Домников Роман'), ('aegorova', 'Егорова Анжелика'), ('ermolovat', 'Ермолова Татьяна'), ('refremov', 'Ефремов Руслан'), ('jarkovan', 'Жаркова Наталья'), ('gukovg', 'Жуков Григорий'), ('gukovau', 'Жукова Юлия'), ('gukovaa', 'Жукова Анна'), ('zabolotiya', 'Заболотный Алексей'), ('zabolotiyd', 'Заболотный Дмитрий'), ('zagorskaya', 'Загорская Юлия'), ('zaycevaa', 'Зайцева Алина'), ('zalubivskiya', 'Залюбовский Алексей'), ('ibragimoval', 'Ибрагимова Лейсан'), ('ivashenko', 'Иващенко Алексей'), ('ivlevan', 'Иевлева Наталья'), ('livina', 'Ильина Людмила'), ('isagadjievag', 'Исагаджиева Гуля'), ('kazancevaa', 'Казанцева Анастасия'), ('kamornikove', 'Каморников Евгений'), ('mkaskov', 'Касков Максим'), ('klimovaf', 'Климкова Валентина'), ('kozus', 'Козусь Анастасия'), ('kolesnika', 'Колесник Алина'), ('kondratovf', 'Кондратов Алексей'), ('konoshece', 'Коношец Елена'), ('crutihinao', 'Крутихина Ольга'), ('kudryavcevao', 'Кудряшова Оксана'), ('kudryashovae', 'Кудряшова Елена'), ('kuznecova', 'Кузнецов Алексей'), ('leontevd', 'Леонтьев Дмитрий'), ('liminae', 'Лимина Елена'), ('lobjanidzev', 'Лобжанидзе Владимир'), ('luganovav', 'Луганова Виктория'), ('makarovam', 'Макарова Марина'), ('maslovam', 'Маслова Марина'), ('maskarao', 'Машкара Оксана'), ('melnichenkon', 'Мельничук Наталья'), ('resep', 'Менеджер Офис'), ('meshkovn', 'Мешков Николай'), ('milovanovv', 'Милованов Виктор'), ('miroshnichenkoi', 'Мирошниченко Ирина'), ('misarovak', 'Мисарова Кристина'), ('mitte', 'Митт Елена'), ('mihailova', 'Михайлов Антон'), ('mihailovau', 'Михайлова Юлия'), ('musaevm', 'Мусаев Мухтар'), ('rnovikov', 'Новиков Роман'), ('novikove', 'Новиков Евгений'), ('novsyanikova', 'Овсянникова Нина'), ('odabashyane', 'Одабащьян Эдуард'), ('vorinchin', 'Оринчин Владимир'), ('aresep', 'Офис Менеджер Адлер'), ('pavlenkoa', 'Павленко Анастасия'), ('panasyka', 'Панасюк Александр'), ('paninv', 'Панин Владислав'), ('perestoroninav', 'Пересторонина Виктория'), ('rpoluvyanov', 'Полувьянов Роман'), ('rudnevae', 'Руднева Елена'), ('savelevv', 'Савельев Евгений'), ('samodelova', 'Самоделов Андрей'), ('samodelovao', 'Самоделова Ольга'), ('samoryadova', 'Саморядов Андрей'), ('seliverstovav', 'Селиверстова Виктория'), ('skripkinaa', 'Скрипкина Анастасия'), ('slavinskayat', 'Славинская Татьяна'), ('slukinam', 'Слукина Марина'), ('isolovova', 'Соловьева Инна'), ('nsolovova', 'Соловьева Наталья'), ('stasukv', 'Стасюк Вячеслав'), ('stepanovao', 'Степанова Ольга'), ('strahovi', 'Страхов Илья'), ('stringinai', 'Стрыгина Ирина'), ('surgutskayao', 'Сургутская Оксана'), ('taskinaa', 'Таскина Анастасия'), ('tretuake', 'Третяк Евгений'), ('tyrins', 'Тюрин Сергей'), ('ushakova', 'Ушаков Антон'), ('fedoseevan', 'Федосеева Надежда'), ('fomine', 'Фомин Евгений'), ('cipurdeyo', 'Ципурдей Олег'), ('cherencovv', 'Черенков '), ('chimbarovv', 'Чимбаров Владимир'), ('shalimovav', 'Шалимова Виктория'), ('shatskayan', 'Шацкая Наталья'), ('strikovv', 'Штрыков Владислав'), ('shtrikovi', 'Штрыков Игорь'), ('shugarinae', 'Шурыгина Елена'), ('yaglova', 'Яглов Алексей')], default=' ', help_text='Необязательно к заполнению', max_length=100, verbose_name='Риелтор в сделке №7'),
        ),
        migrations.AlterField(
            model_name='otchet_nov',
            name='reelt8',
            field=models.CharField(blank=True, choices=[('zalubovskiya', ' '), ('seo', ' '), ('demo', 'demon demo'), ('alekseevau', 'Алексеева Юлия'), ('belyaevd', 'Беляев Дмитрий'), ('belyaevag', 'Беляева Галина'), ('vinnikovao', 'Винникова Анастасия'), ('vishnevskiya', 'Вишневецкий Александр'), ('gainullini', 'Гайнуллин Иван'), ('golovind', 'Головин Дмитрий'), ('deminaa', 'Демина Анжелика'), ('ujashakueva', 'Джашакуева Римма'), ('dogadinau', 'Догадина Юлия'), ('homka', 'Домников Роман'), ('aegorova', 'Егорова Анжелика'), ('ermolovat', 'Ермолова Татьяна'), ('refremov', 'Ефремов Руслан'), ('jarkovan', 'Жаркова Наталья'), ('gukovg', 'Жуков Григорий'), ('gukovau', 'Жукова Юлия'), ('gukovaa', 'Жукова Анна'), ('zabolotiya', 'Заболотный Алексей'), ('zabolotiyd', 'Заболотный Дмитрий'), ('zagorskaya', 'Загорская Юлия'), ('zaycevaa', 'Зайцева Алина'), ('zalubivskiya', 'Залюбовский Алексей'), ('ibragimoval', 'Ибрагимова Лейсан'), ('ivashenko', 'Иващенко Алексей'), ('ivlevan', 'Иевлева Наталья'), ('livina', 'Ильина Людмила'), ('isagadjievag', 'Исагаджиева Гуля'), ('kazancevaa', 'Казанцева Анастасия'), ('kamornikove', 'Каморников Евгений'), ('mkaskov', 'Касков Максим'), ('klimovaf', 'Климкова Валентина'), ('kozus', 'Козусь Анастасия'), ('kolesnika', 'Колесник Алина'), ('kondratovf', 'Кондратов Алексей'), ('konoshece', 'Коношец Елена'), ('crutihinao', 'Крутихина Ольга'), ('kudryavcevao', 'Кудряшова Оксана'), ('kudryashovae', 'Кудряшова Елена'), ('kuznecova', 'Кузнецов Алексей'), ('leontevd', 'Леонтьев Дмитрий'), ('liminae', 'Лимина Елена'), ('lobjanidzev', 'Лобжанидзе Владимир'), ('luganovav', 'Луганова Виктория'), ('makarovam', 'Макарова Марина'), ('maslovam', 'Маслова Марина'), ('maskarao', 'Машкара Оксана'), ('melnichenkon', 'Мельничук Наталья'), ('resep', 'Менеджер Офис'), ('meshkovn', 'Мешков Николай'), ('milovanovv', 'Милованов Виктор'), ('miroshnichenkoi', 'Мирошниченко Ирина'), ('misarovak', 'Мисарова Кристина'), ('mitte', 'Митт Елена'), ('mihailova', 'Михайлов Антон'), ('mihailovau', 'Михайлова Юлия'), ('musaevm', 'Мусаев Мухтар'), ('rnovikov', 'Новиков Роман'), ('novikove', 'Новиков Евгений'), ('novsyanikova', 'Овсянникова Нина'), ('odabashyane', 'Одабащьян Эдуард'), ('vorinchin', 'Оринчин Владимир'), ('aresep', 'Офис Менеджер Адлер'), ('pavlenkoa', 'Павленко Анастасия'), ('panasyka', 'Панасюк Александр'), ('paninv', 'Панин Владислав'), ('perestoroninav', 'Пересторонина Виктория'), ('rpoluvyanov', 'Полувьянов Роман'), ('rudnevae', 'Руднева Елена'), ('savelevv', 'Савельев Евгений'), ('samodelova', 'Самоделов Андрей'), ('samodelovao', 'Самоделова Ольга'), ('samoryadova', 'Саморядов Андрей'), ('seliverstovav', 'Селиверстова Виктория'), ('skripkinaa', 'Скрипкина Анастасия'), ('slavinskayat', 'Славинская Татьяна'), ('slukinam', 'Слукина Марина'), ('isolovova', 'Соловьева Инна'), ('nsolovova', 'Соловьева Наталья'), ('stasukv', 'Стасюк Вячеслав'), ('stepanovao', 'Степанова Ольга'), ('strahovi', 'Страхов Илья'), ('stringinai', 'Стрыгина Ирина'), ('surgutskayao', 'Сургутская Оксана'), ('taskinaa', 'Таскина Анастасия'), ('tretuake', 'Третяк Евгений'), ('tyrins', 'Тюрин Сергей'), ('ushakova', 'Ушаков Антон'), ('fedoseevan', 'Федосеева Надежда'), ('fomine', 'Фомин Евгений'), ('cipurdeyo', 'Ципурдей Олег'), ('cherencovv', 'Черенков '), ('chimbarovv', 'Чимбаров Владимир'), ('shalimovav', 'Шалимова Виктория'), ('shatskayan', 'Шацкая Наталья'), ('strikovv', 'Штрыков Владислав'), ('shtrikovi', 'Штрыков Игорь'), ('shugarinae', 'Шурыгина Елена'), ('yaglova', 'Яглов Алексей')], default=' ', help_text='Необязательно к заполнению', max_length=100, verbose_name='Риелтор в сделке №8'),
        ),
        migrations.AlterField(
            model_name='otchet_nov',
            name='reelt9',
            field=models.CharField(blank=True, choices=[('zalubovskiya', ' '), ('seo', ' '), ('demo', 'demon demo'), ('alekseevau', 'Алексеева Юлия'), ('belyaevd', 'Беляев Дмитрий'), ('belyaevag', 'Беляева Галина'), ('vinnikovao', 'Винникова Анастасия'), ('vishnevskiya', 'Вишневецкий Александр'), ('gainullini', 'Гайнуллин Иван'), ('golovind', 'Головин Дмитрий'), ('deminaa', 'Демина Анжелика'), ('ujashakueva', 'Джашакуева Римма'), ('dogadinau', 'Догадина Юлия'), ('homka', 'Домников Роман'), ('aegorova', 'Егорова Анжелика'), ('ermolovat', 'Ермолова Татьяна'), ('refremov', 'Ефремов Руслан'), ('jarkovan', 'Жаркова Наталья'), ('gukovg', 'Жуков Григорий'), ('gukovau', 'Жукова Юлия'), ('gukovaa', 'Жукова Анна'), ('zabolotiya', 'Заболотный Алексей'), ('zabolotiyd', 'Заболотный Дмитрий'), ('zagorskaya', 'Загорская Юлия'), ('zaycevaa', 'Зайцева Алина'), ('zalubivskiya', 'Залюбовский Алексей'), ('ibragimoval', 'Ибрагимова Лейсан'), ('ivashenko', 'Иващенко Алексей'), ('ivlevan', 'Иевлева Наталья'), ('livina', 'Ильина Людмила'), ('isagadjievag', 'Исагаджиева Гуля'), ('kazancevaa', 'Казанцева Анастасия'), ('kamornikove', 'Каморников Евгений'), ('mkaskov', 'Касков Максим'), ('klimovaf', 'Климкова Валентина'), ('kozus', 'Козусь Анастасия'), ('kolesnika', 'Колесник Алина'), ('kondratovf', 'Кондратов Алексей'), ('konoshece', 'Коношец Елена'), ('crutihinao', 'Крутихина Ольга'), ('kudryavcevao', 'Кудряшова Оксана'), ('kudryashovae', 'Кудряшова Елена'), ('kuznecova', 'Кузнецов Алексей'), ('leontevd', 'Леонтьев Дмитрий'), ('liminae', 'Лимина Елена'), ('lobjanidzev', 'Лобжанидзе Владимир'), ('luganovav', 'Луганова Виктория'), ('makarovam', 'Макарова Марина'), ('maslovam', 'Маслова Марина'), ('maskarao', 'Машкара Оксана'), ('melnichenkon', 'Мельничук Наталья'), ('resep', 'Менеджер Офис'), ('meshkovn', 'Мешков Николай'), ('milovanovv', 'Милованов Виктор'), ('miroshnichenkoi', 'Мирошниченко Ирина'), ('misarovak', 'Мисарова Кристина'), ('mitte', 'Митт Елена'), ('mihailova', 'Михайлов Антон'), ('mihailovau', 'Михайлова Юлия'), ('musaevm', 'Мусаев Мухтар'), ('rnovikov', 'Новиков Роман'), ('novikove', 'Новиков Евгений'), ('novsyanikova', 'Овсянникова Нина'), ('odabashyane', 'Одабащьян Эдуард'), ('vorinchin', 'Оринчин Владимир'), ('aresep', 'Офис Менеджер Адлер'), ('pavlenkoa', 'Павленко Анастасия'), ('panasyka', 'Панасюк Александр'), ('paninv', 'Панин Владислав'), ('perestoroninav', 'Пересторонина Виктория'), ('rpoluvyanov', 'Полувьянов Роман'), ('rudnevae', 'Руднева Елена'), ('savelevv', 'Савельев Евгений'), ('samodelova', 'Самоделов Андрей'), ('samodelovao', 'Самоделова Ольга'), ('samoryadova', 'Саморядов Андрей'), ('seliverstovav', 'Селиверстова Виктория'), ('skripkinaa', 'Скрипкина Анастасия'), ('slavinskayat', 'Славинская Татьяна'), ('slukinam', 'Слукина Марина'), ('isolovova', 'Соловьева Инна'), ('nsolovova', 'Соловьева Наталья'), ('stasukv', 'Стасюк Вячеслав'), ('stepanovao', 'Степанова Ольга'), ('strahovi', 'Страхов Илья'), ('stringinai', 'Стрыгина Ирина'), ('surgutskayao', 'Сургутская Оксана'), ('taskinaa', 'Таскина Анастасия'), ('tretuake', 'Третяк Евгений'), ('tyrins', 'Тюрин Сергей'), ('ushakova', 'Ушаков Антон'), ('fedoseevan', 'Федосеева Надежда'), ('fomine', 'Фомин Евгений'), ('cipurdeyo', 'Ципурдей Олег'), ('cherencovv', 'Черенков '), ('chimbarovv', 'Чимбаров Владимир'), ('shalimovav', 'Шалимова Виктория'), ('shatskayan', 'Шацкая Наталья'), ('strikovv', 'Штрыков Владислав'), ('shtrikovi', 'Штрыков Игорь'), ('shugarinae', 'Шурыгина Елена'), ('yaglova', 'Яглов Алексей')], default=' ', help_text='Необязательно к заполнению', max_length=100, verbose_name='Риелтор в сделке №9'),
        ),
    ]