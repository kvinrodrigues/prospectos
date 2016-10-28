# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulo', '0002_articulo_articulo_target_contact'),
        ('vendedor', '0001_initial'),
        ('campanha', '0003_campanha_vende'),
    ]

    operations = [
        migrations.AddField(
            model_name='campanha',
            name='arti',
            field=models.ManyToManyField(to='articulo.Articulo', null=True),
        ),
        migrations.RemoveField(
            model_name='campanha',
            name='vende',
        ),
        migrations.AddField(
            model_name='campanha',
            name='vende',
            field=models.ManyToManyField(to='vendedor.Vendedor', null=True),
        ),
    ]
