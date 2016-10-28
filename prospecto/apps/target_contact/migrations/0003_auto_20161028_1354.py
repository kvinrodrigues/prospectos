# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulo', '0001_initial'),
        ('target_contact', '0002_auto_20161028_1316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='target_contact',
            name='art',
        ),
        migrations.AddField(
            model_name='target_contact',
            name='art',
            field=models.ManyToManyField(to='articulo.Articulo'),
        ),
    ]
