# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('remote', '0002_featurefieldrel_collect_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featurefieldrel',
            name='collect_type',
            field=models.CharField(max_length=64, null=True, verbose_name='\u6570\u636e\u83b7\u53d6\u65b9\u5f0f'),
            preserve_default=True,
        ),
    ]
