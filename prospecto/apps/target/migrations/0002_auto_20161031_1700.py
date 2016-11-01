# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('target', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='target',
            old_name='idTarger',
            new_name='idTarget',
        ),
    ]
