# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-10-15 15:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basicviz', '0083_auto_20181015_1525'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeatureInstance2Sub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fragatoms', models.CharField(max_length=128)),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basicviz.FeatureInstance')),
                ('sub', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basicviz.MagmaSub')),
            ],
        ),
        migrations.RemoveField(
            model_name='docfeature2sub',
            name='document',
        ),
        migrations.RemoveField(
            model_name='docfeature2sub',
            name='feature',
        ),
        migrations.RemoveField(
            model_name='docfeature2sub',
            name='sub',
        ),
        migrations.DeleteModel(
            name='DocFeature2Sub',
        ),
    ]
