# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendedor', '0001_initial'),
        ('campanha', '0002_auto_20161028_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='campanha',
            name='vende',
            field=models.ForeignKey(to='vendedor.Vendedor', null=True),
        ),
    ]
