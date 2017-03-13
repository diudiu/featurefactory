# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etl', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='featureconf',
            name='feature_type',
            field=models.IntegerField(null=True, verbose_name='\u7279\u5f81\u7c7b\u578b'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='featureconf',
            name='feature_type_desc',
            field=models.CharField(max_length=2048, null=True, verbose_name='\u7279\u5f81\u7c7b\u578b\u89e3\u91ca'),
            preserve_default=True,
        ),
    ]
