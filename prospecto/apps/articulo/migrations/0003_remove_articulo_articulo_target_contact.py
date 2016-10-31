# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulo', '0002_articulo_articulo_target_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articulo',
            name='articulo_target_contact',
        ),
    ]
