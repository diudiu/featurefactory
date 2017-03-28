# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etl', '0015_auto_20170327_1012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='featurerelevanceconf',
            name='depend_di',
        ),
    ]
