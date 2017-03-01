# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 19:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicviz', '0053_auto_20170226_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiment',
            name='K',
            field=models.IntegerField(default=300, null=True),
        ),
        migrations.AddField(
            model_name='experiment',
            name='isolation_window',
            field=models.FloatField(default=0.5, null=True),
        ),
        migrations.AddField(
            model_name='experiment',
            name='max_ms1_rt',
            field=models.FloatField(default=21, null=True),
        ),
        migrations.AddField(
            model_name='experiment',
            name='min_ms1_rt',
            field=models.FloatField(default=3, null=True),
        ),
        migrations.AddField(
            model_name='experiment',
            name='min_ms2_intensity',
            field=models.FloatField(default=5000, null=True),
        ),
        migrations.AddField(
            model_name='experiment',
            name='mz_tol',
            field=models.FloatField(default=5, null=True),
        ),
        migrations.AddField(
            model_name='experiment',
            name='rt_tol',
            field=models.FloatField(default=10, null=True),
        ),
    ]