# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etl', '0013_auto_20170324_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prefieldinfo',
            name='path',
            field=models.CharField(max_length=256, null=True, verbose_name='JsonPath\u8def\u5f84'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='prefieldinfo',
            name='source',
            field=models.CharField(max_length=64, null=True, verbose_name='\u6570\u636e\u6765\u6e90'),
            preserve_default=True,
        ),
    ]
