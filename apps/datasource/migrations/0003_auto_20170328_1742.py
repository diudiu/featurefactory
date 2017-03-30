# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datasource', '0002_dsinterfaceinfo_data_origin_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dsinterfaceinfo',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='dsinterfaceinfo',
            name='common_data',
        ),
    ]
