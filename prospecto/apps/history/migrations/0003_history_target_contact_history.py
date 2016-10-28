# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('target_contact', '0002_auto_20161028_1316'),
        ('history', '0002_auto_20161028_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='Target_Contact_history',
            field=models.ForeignKey(related_name='Target_Contact_history', to='target_contact.Target_Contact', null=True),
        ),
    ]
