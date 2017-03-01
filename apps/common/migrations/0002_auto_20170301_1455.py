# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='featurecodemapping',
            name='arithmetic_type',
            field=models.CharField(max_length=16, null=True, verbose_name=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='featurecodemapping',
            name='feature_desc',
            field=models.CharField(max_length=128, null=True, verbose_name='\u7279\u5f81\u4e2d\u6587\u89e3\u91ca'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='featurecodemapping',
            name='id',
            field=models.AutoField(serialize=False, verbose_name='\u4e3b\u952e', primary_key=True),
            preserve_default=True,
        ),
    ]
