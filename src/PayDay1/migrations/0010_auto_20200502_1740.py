# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-02 17:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PayDay1', '0009_user_is_manager'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='job',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='job_complete',
        ),
    ]
