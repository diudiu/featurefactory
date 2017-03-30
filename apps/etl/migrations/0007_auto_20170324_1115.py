# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etl', '0006_remove_featureconf_data_identity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='featureconf',
            old_name='raw_field_name',
            new_name='data_identity',
        ),
    ]
