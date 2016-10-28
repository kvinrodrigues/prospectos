# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supervisor', '0001_initial'),
        ('vendedor', '0001_initial'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='usuario_supervisor',
            field=models.OneToOneField(null=True, to='supervisor.Supervisor'),
        ),
        migrations.AddField(
            model_name='usuarios',
            name='usuario_vendedor',
            field=models.OneToOneField(null=True, to='vendedor.Vendedor'),
        ),
    ]
