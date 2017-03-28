# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etl', '0016_remove_featurerelevanceconf_depend_di'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='featureprocess',
            name='map_and_filter_chain',
        ),
        migrations.AddField(
            model_name='featureprocess',
            name='f_map_and_filter_chain',
            field=models.CharField(max_length=1024, null=True, verbose_name='\u7279\u5f81\u5904\u7406\u524d\u7f6emap\u94fe'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='featureprocess',
            name='l_map_and_filter_chain',
            field=models.CharField(max_length=1024, null=True, verbose_name='\u7279\u5f81\u5904\u7406\u540e\u7f6emap\u94fe'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='featureprocess',
            name='reduce_chain',
            field=models.CharField(max_length=1024, null=True, verbose_name='\u7279\u5f81\u5904\u7406reduce\u94fe'),
            preserve_default=True,
        ),
    ]
