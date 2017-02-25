# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etl', '0002_auto_20170223_1027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='featureconf',
            name='data_origin_type',
        ),
    ]
