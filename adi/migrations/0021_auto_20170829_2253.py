# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-29 22:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adi', '0020_auto_20170824_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='estado',
            field=models.CharField(max_length=14),
        ),
    ]
