# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etl', '0002_auto_20170313_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='featureconf',
            name='feature_card_type',
            field=models.IntegerField(null=True, verbose_name='\u7279\u5f81\u8bc4\u5206\u5361\u7c7b\u578b'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='featureconf',
            name='feature_card_type_desc',
            field=models.CharField(max_length=2048, null=True, verbose_name='\u7279\u5f81\u8bc4\u5206\u5361\u7c7b\u578b\u89e3\u91ca'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='featureconf',
            name='feature_rule_type',
            field=models.IntegerField(null=True, verbose_name='\u7279\u5f81\u89c4\u5219\u7c7b\u578b'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='featureconf',
            name='feature_rule_type_desc',
            field=models.CharField(max_length=2048, null=True, verbose_name='\u7279\u5f81\u89c4\u5219\u7c7b\u578b\u89e3\u91ca'),
            preserve_default=True,
        ),
    ]
