# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etl', '0019_auto_20170328_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featureprocess',
            name='feature_name',
            field=models.CharField(unique=True, max_length=100, verbose_name='\u7279\u5f81\u5b57\u6bb5\u540d'),
            preserve_default=True,
        ),
    ]
