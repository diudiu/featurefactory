# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etl', '0005_auto_20170324_1110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='featureconf',
            name='data_identity',
        ),
    ]
