# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-18 06:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trails', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trail',
            name='ascent',
            field=models.IntegerField(blank=True, help_text='Stored as meters', null=True),
        ),
        migrations.AlterField(
            model_name='trail',
            name='distance',
            field=models.IntegerField(blank=True, help_text='Stored as meters', null=True),
        ),
    ]