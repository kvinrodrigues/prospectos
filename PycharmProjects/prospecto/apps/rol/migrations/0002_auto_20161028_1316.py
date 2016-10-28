# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rol', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rol',
            name='usuario',
            field=models.ForeignKey(to='usuarios.Usuarios'),
        ),
    ]
