# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idVendedor', models.IntegerField()),
                ('nombreVendedor', models.CharField(max_length=80)),
                ('telefonoVendedor', models.IntegerField()),
            ],
        ),
    ]
