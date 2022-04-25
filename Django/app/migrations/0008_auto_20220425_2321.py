# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-04-25 20:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20220424_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2022, 4, 25, 23, 21, 29, 281659), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2022, 4, 25, 23, 21, 29, 282626), verbose_name='Дата комментария'),
        ),
    ]