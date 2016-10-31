# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendedor', '0003_auto_20161031_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendedor',
            name='vendedor_supervisor',
            field=models.ForeignKey(to='supervisor.Supervisor', null=True),
        ),
    ]
