# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-16 13:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articulo', '0008_historicalarticulo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalarticulo',
            name='history_user',
        ),
        migrations.DeleteModel(
            name='HistoricalArticulo',
        ),
    ]
