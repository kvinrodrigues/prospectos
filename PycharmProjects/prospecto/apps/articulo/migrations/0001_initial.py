# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idArticulo', models.IntegerField()),
                ('descripcionArticulo', models.TextField(max_length=200)),
                ('tipoArticulo', models.CharField(max_length=80)),
                ('montoArticulo', models.IntegerField()),
                ('disponibilidad', models.IntegerField()),
            ],
        ),
    ]
