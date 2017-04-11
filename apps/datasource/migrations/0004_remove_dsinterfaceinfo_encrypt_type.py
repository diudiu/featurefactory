# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datasource', '0003_auto_20170328_1742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dsinterfaceinfo',
            name='encrypt_type',
        ),
    ]
