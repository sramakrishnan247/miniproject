# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-25 17:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_landowner_pincode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landowner',
            name='pincode',
            field=models.IntegerField(),
        ),
    ]
