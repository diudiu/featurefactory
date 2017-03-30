# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etl', '0018_auto_20170328_1508'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='featureprocess',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='featureprocess',
            name='is_delete',
        ),
        migrations.RemoveField(
            model_name='featureprocess',
            name='updated_on',
        ),
        migrations.AlterField(
            model_name='featureprocess',
            name='default_value',
            field=models.CharField(max_length=100, verbose_name='\u7279\u5f81\u7f3a\u7701\u503c'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='featureprocess',
            name='f_map_and_filter_chain',
            field=models.CharField(max_length=2048, null=True, verbose_name='\u7279\u5f81\u5904\u7406\u524d\u7f6emap\u94fe'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='featureprocess',
            name='feature_data_type',
            field=models.CharField(max_length=50, verbose_name='\u7279\u5f81\u5b57\u6bb5\u7c7b\u578b'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='featureprocess',
            name='feature_name',
            field=models.CharField(max_length=500, verbose_name='\u7279\u5f81\u5b57\u6bb5\u540d'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='featureprocess',
            name='l_map_and_filter_chain',
            field=models.CharField(max_length=2048, null=True, verbose_name='\u7279\u5f81\u5904\u7406\u540e\u7f6emap\u94fe'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='featureprocess',
            name='reduce_chain',
            field=models.CharField(max_length=2048, null=True, verbose_name='\u7279\u5f81\u5904\u7406reduce\u94fe'),
            preserve_default=True,
        ),
    ]
