# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etl', '0014_auto_20170324_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featureconf',
            name='data_identity',
            field=models.CharField(max_length=2048, null=True, verbose_name='\u53c2\u6570\u5b57\u6bb5\u540d'),
            preserve_default=True,
        ),
    ]
