# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-17 07:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import trails.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Trail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('region', models.CharField(blank=True, help_text='e.g. Yosemite, CA', max_length=120, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('trackfile', models.FileField(blank=True, null=True, upload_to=trails.models.get_gpx_path)),
                ('distance', models.DecimalField(blank=True, decimal_places=2, help_text='Stored as meters', max_digits=7, null=True)),
                ('ascent', models.DecimalField(blank=True, decimal_places=2, help_text='Stored as meters', max_digits=5, null=True)),
                ('calories', models.SmallIntegerField(blank=True, null=True)),
                ('duration', models.DurationField(blank=True, null=True)),
                ('geocaches', models.BooleanField(default=False, help_text='Geocaches available on this trail')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
