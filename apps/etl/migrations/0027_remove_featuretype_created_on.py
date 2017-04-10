# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etl', '0026_featuretype_created_on'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='featuretype',
            name='created_on',
        ),
    ]
