# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-21 12:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendee',
            name='event_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.EventUser', verbose_name='Event User'),
        ),
    ]
