# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etl', '0022_auto_20170329_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featureprocess',
            name='json_path_list',
            field=models.TextField(null=True, verbose_name='\u7279\u5f81\u5904\u7406\u6d41\u7a0b'),
            preserve_default=True,
        ),
    ]
