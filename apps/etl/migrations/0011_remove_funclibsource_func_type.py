# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etl', '0010_auto_20170324_1526'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funclibsource',
            name='func_type',
        ),
    ]
