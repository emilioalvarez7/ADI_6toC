# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-29 17:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adi', '0002_auto_20170729_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preceptor',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]