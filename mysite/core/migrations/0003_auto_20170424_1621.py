# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-24 16:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20170423_0610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carowner',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='carowner',
            name='location',
        ),
        migrations.RemoveField(
            model_name='landowner',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='landowner',
            name='birth_date',
        ),
        migrations.AddField(
            model_name='carowner',
            name='Name',
            field=models.CharField(blank=True, max_length=70),
        ),
        migrations.AddField(
            model_name='carowner',
            name='email',
            field=models.EmailField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='landowner',
            name='email',
            field=models.EmailField(blank=True, max_length=50),
        ),
    ]