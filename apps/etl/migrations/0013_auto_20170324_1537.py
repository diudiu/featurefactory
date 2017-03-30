# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etl', '0012_funclibsource_func_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funclibsource',
            name='func_type',
            field=models.CharField(default=b'M', max_length=10, verbose_name='\u51fd\u6570\u7c7b\u578b', db_index=True, choices=[(b'M', 'map'), (b'F', 'filter'), (b'R', 'reduce'), (b'A', 'assert')]),
            preserve_default=True,
        ),
    ]
