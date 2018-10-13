# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-08-16 09:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0103_flat_obj_vestum_pub'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otchet_nov',
            name='ot_kuda_kl',
            field=models.CharField(choices=[('Другое', 'Другое'), ('Avito', 'Avito'), ('Vestum', 'Vestum'), ('Cian', 'Cian'), ('Сайт компании', 'Сайт компании'), ('По рекомендации', 'По рекомендации'), ('Домклик(Сбер)', 'Домклик(Сбер)'), ('Yandex Недвижимость', 'Yandex Недвижимость')], max_length=20, verbose_name='Канал привлечения клиента:'),
        ),
    ]
