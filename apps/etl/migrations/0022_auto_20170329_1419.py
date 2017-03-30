# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etl', '0021_auto_20170328_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funclibsource',
            name='func_desc',
            field=models.TextField(null=True, verbose_name='\u51fd\u6570\u63cf\u8ff0'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='funclibsource',
            name='func_name',
            field=models.CharField(max_length=80, serialize=False, verbose_name='\u51fd\u6570\u540d', primary_key=True),
            preserve_default=True,
        ),
    ]
