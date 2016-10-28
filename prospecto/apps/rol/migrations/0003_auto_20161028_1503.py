# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rol', '0002_auto_20161028_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rol',
            name='usuario',
            field=models.OneToOneField(to='usuarios.Usuarios'),
        ),
    ]
