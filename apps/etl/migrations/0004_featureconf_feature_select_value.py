# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etl', '0003_auto_20170320_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='featureconf',
            name='feature_select_value',
            field=models.CharField(max_length=2048, null=True, verbose_name='\u7279\u5f81\u53ef\u9009\u503c'),
            preserve_default=True,
        ),
    ]
