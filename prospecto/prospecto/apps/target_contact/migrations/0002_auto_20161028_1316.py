# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('target', '0001_initial'),
        ('articulo', '0001_initial'),
        ('vendedor', '0001_initial'),
        ('target_contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Target_Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idTarget_Contact', models.IntegerField()),
                ('art', models.ForeignKey(to='articulo.Articulo')),
                ('objetivo', models.ForeignKey(to='target.Target')),
                ('vende', models.ForeignKey(to='vendedor.Vendedor')),
            ],
        ),
        migrations.DeleteModel(
            name='Histoty',
        ),
    ]
