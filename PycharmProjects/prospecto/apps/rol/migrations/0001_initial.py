# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idRol', models.IntegerField()),
                ('descripcionRol', models.TextField()),
                ('tipoRol', models.CharField(max_length=15)),
                ('usuario', models.OneToOneField(to='usuarios.Usuarios')),
            ],
        ),
    ]
