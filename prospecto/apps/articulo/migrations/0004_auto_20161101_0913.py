# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulo', '0003_remove_articulo_articulo_target_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='nombreArticulo',
            field=models.TextField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='descripcionArticulo',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
