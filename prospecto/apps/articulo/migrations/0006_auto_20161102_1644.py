# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-02 19:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulo', '0005_remove_articulo_idarticulo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articulo',
            name='descripcionArticulo',
        ),
        migrations.AlterField(
            model_name='articulo',
            name='tipoArticulo',
            field=models.CharField(max_length=80, null=True),
        ),
    ]