# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-07-01 13:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicviz', '0089_experiment_include_motifset'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment',
            name='experiment_ms2_format',
            field=models.CharField(choices=[(b'0', b'mzML'), (b'1', b'msp'), (b'2', b'mgf'), (b'3', b'upload'), (b'4', b'uploadgensim')], default=b'0', max_length=128, null=True),
        ),
    ]