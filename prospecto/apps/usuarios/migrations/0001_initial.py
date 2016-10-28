# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idUsuario', models.IntegerField()),
                ('nombreUsuario', models.CharField(max_length=20)),
                ('passUsuario', models.CharField(max_length=20)),
            ],
        ),
    ]
