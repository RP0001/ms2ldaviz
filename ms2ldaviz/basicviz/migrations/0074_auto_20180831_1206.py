# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-08-31 12:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicviz', '0073_auto_20180831_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiment',
            name='csv_id_column',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='experiment',
            name='ms2_id_field',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
