# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-02 16:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('target_contact', '0004_auto_20161028_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='target_contact',
            name='Articulo',
            field=models.ManyToManyField(to='articulo.Articulo'),
        ),
    ]
