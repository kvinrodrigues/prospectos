# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='articulo_target_contact',
            field=models.IntegerField(null=True),
        ),
    ]
