# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 23:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_auto_20170828_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
    ]
