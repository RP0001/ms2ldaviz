# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-10-15 15:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basicviz', '0082_auto_20181010_1010'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocFeature2Sub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fragatoms', models.CharField(max_length=128)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basicviz.Document')),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basicviz.FeatureInstance')),
            ],
        ),
        migrations.RemoveField(
            model_name='doc2sub',
            name='document',
        ),
        migrations.RemoveField(
            model_name='doc2sub',
            name='sub',
        ),
        migrations.AlterField(
            model_name='magmasub',
            name='mol_string',
            field=models.TextField(null=True),
        ),
        migrations.DeleteModel(
            name='Doc2Sub',
        ),
        migrations.AddField(
            model_name='docfeature2sub',
            name='sub',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basicviz.MagmaSub'),
        ),
    ]
