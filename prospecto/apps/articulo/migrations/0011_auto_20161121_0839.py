# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-21 11:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articulo', '0010_auto_20161118_1551'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articulo',
            options={'permissions': (('can_add_articulo', 'Puede agregar articulo'),)},
        ),
    ]
