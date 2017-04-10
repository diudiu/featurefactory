# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etl', '0025_auto_20170410_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='featuretype',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4', null=True),
            preserve_default=True,
        ),
    ]
