# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-20 12:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adi', '0030_auto_20170914_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='tipo',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]