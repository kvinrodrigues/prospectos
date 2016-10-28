# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulo', '0002_articulo_articulo_target_contact'),
        ('target', '0001_initial'),
        ('vendedor', '0001_initial'),
        ('target_contact', '0003_auto_20161028_1354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='target_contact',
            name='art',
        ),
        migrations.RemoveField(
            model_name='target_contact',
            name='objetivo',
        ),
        migrations.RemoveField(
            model_name='target_contact',
            name='vende',
        ),
        migrations.AddField(
            model_name='target_contact',
            name='Articulo',
            field=models.ManyToManyField(to='articulo.Articulo', null=True),
        ),
        migrations.AddField(
            model_name='target_contact',
            name='Objetivo',
            field=models.ForeignKey(to='target.Target', null=True),
        ),
        migrations.AddField(
            model_name='target_contact',
            name='Vendedor',
            field=models.ForeignKey(to='vendedor.Vendedor', null=True),
        ),
    ]
