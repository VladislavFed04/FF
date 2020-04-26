# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-22 15:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200422_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.FileField(default='temp.jpg', upload_to='', verbose_name='Путь к картинке'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 4, 22, 18, 9, 18, 336392), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='data',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 4, 22, 18, 9, 18, 338393), verbose_name='Дата'),
        ),
    ]
