# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-03-07 13:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('motifdb', '0003_auto_20190307_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='mdbmotifset',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
