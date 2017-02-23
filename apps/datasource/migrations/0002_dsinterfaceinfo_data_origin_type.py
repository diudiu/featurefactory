# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datasource', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dsinterfaceinfo',
            name='data_origin_type',
            field=models.IntegerField(null=True, verbose_name='\u6570\u636e\u6e90\u6807\u8bb0'),
            preserve_default=True,
        ),
    ]
