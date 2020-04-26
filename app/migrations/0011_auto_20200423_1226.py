# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-23 09:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20200423_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 4, 23, 12, 26, 29, 184769), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='data',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 4, 23, 12, 26, 29, 184769), verbose_name='Дата'),
        ),
    ]
