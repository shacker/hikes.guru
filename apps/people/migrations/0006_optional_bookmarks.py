# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-17 07:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0005_userprofile_allow_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='allow_contact',
            field=models.BooleanField(default=True, help_text='Allow site members to contact me with questions about trails (without sharing my email).'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='bookmarks',
            field=models.ManyToManyField(blank=True, null=True, to='trails.Trail'),
        ),
    ]
