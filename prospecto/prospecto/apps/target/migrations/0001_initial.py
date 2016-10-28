# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idTarger', models.IntegerField()),
                ('nombreTarget', models.CharField(max_length=80)),
                ('telefonoTarget', models.IntegerField()),
                ('origenTarget', models.CharField(max_length=80)),
                ('estadoTarget', models.BooleanField()),
            ],
        ),
    ]
