# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-05 05:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20170504_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landowner',
            name='placename',
            field=models.CharField(max_length=40),
        ),
    ]
