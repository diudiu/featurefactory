# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_auto_20170301_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featurecodemapping',
            name='dual_value',
            field=models.CharField(max_length=64, null=True, verbose_name='\u53d6\u503c\u7684\u6700\u5927\u503c'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='featurecodemapping',
            name='unitary_value',
            field=models.CharField(max_length=64, verbose_name='\u53d6\u503c\u57fa\u51c6\u503c'),
            preserve_default=True,
        ),
    ]
