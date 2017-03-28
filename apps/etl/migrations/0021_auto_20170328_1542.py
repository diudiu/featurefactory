# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etl', '0020_auto_20170328_1521'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funclibsource',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='funclibsource',
            name='is_delete',
        ),
        migrations.RemoveField(
            model_name='funclibsource',
            name='updated_on',
        ),
        migrations.AlterField(
            model_name='funclibsource',
            name='func_desc',
            field=models.CharField(max_length=2048, null=True, verbose_name='\u51fd\u6570\u63cf\u8ff0'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='funclibsource',
            name='func_name',
            field=models.CharField(max_length=100, serialize=False, verbose_name='\u51fd\u6570\u540d', primary_key=True),
            preserve_default=True,
        ),
    ]
