# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supervisor', '0001_initial'),
        ('vendedor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendedor',
            name='vendedor_supervisor',
            field=models.ForeignKey(to='supervisor.Supervisor', null=True),
        ),
    ]
