# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-02 18:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PayDay1', '0014_auto_20200502_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='user',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]