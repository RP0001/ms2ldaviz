# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-15 18:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basicviz', '0068_auto_20170509_2103'),
    ]

    operations = [
        migrations.CreateModel(
            name='BVFeatureSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='feature',
            name='experiment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='basicviz.Experiment'),
        ),
        migrations.AddField(
            model_name='feature',
            name='featureset',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='basicviz.BVFeatureSet'),
        ),
    ]