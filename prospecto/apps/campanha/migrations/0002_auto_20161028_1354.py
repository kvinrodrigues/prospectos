# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campanha', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campanha',
            name='descripcionCampanha',
            field=models.TextField(),
        ),
    ]
