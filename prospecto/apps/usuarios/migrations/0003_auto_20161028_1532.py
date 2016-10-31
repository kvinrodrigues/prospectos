# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20161028_1503'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuarios',
            name='usuario_supervisor',
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='usuario_vendedor',
        ),
    ]
