# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-26 21:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('PayDay1', '0006_auto_20200426_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timesheet',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
