# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-22 21:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20200422_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 4, 23, 0, 12, 55, 968153), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='data',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 4, 23, 0, 12, 55, 969166), verbose_name='Дата'),
        ),
    ]
