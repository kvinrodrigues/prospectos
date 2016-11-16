# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-16 13:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('target', '0004_auto_20161102_1655'),
        ('vendedor', '0006_historicalvendedor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalvendedor',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicalvendedor',
            name='vendedor_supervisor',
        ),
        migrations.AddField(
            model_name='vendedor',
            name='targetToCall',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='target.Target'),
        ),
        migrations.DeleteModel(
            name='HistoricalVendedor',
        ),
    ]
