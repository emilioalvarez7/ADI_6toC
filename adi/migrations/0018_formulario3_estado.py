# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-17 14:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adi', '0017_formulario2_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='formulario3',
            name='estado',
            field=models.CharField(default=534, max_length=8),
            preserve_default=False,
        ),
    ]