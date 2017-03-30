# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etl', '0011_remove_funclibsource_func_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='funclibsource',
            name='func_type',
            field=models.CharField(default=b'1', max_length=10, verbose_name='\u51fd\u6570\u7c7b\u578b', db_index=True, choices=[(b'1', 'map'), (b'2', 'filter'), (b'3', 'reduce'), (b'4', 'assert')]),
            preserve_default=True,
        ),
    ]
