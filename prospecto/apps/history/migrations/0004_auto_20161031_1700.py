# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0003_history_target_contact_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='descripcionHistorial',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='history',
            name='fechaHistorial',
            field=models.DateField(null=True),
        ),
    ]
