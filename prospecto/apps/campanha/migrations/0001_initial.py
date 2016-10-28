# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campanha',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idCampanha', models.IntegerField()),
                ('descripcionCampanha', models.IntegerField(max_length=200)),
                ('fecha_inicio_Campanha', models.DateField()),
                ('fecha_fin_Campanha', models.DateField()),
                ('porcentajeCampanha', models.IntegerField()),
            ],
        ),
    ]
