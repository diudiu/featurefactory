# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datasource', '0004_remove_dsinterfaceinfo_encrypt_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='dsinterfaceinfo',
            name='encrypt_type',
            field=models.CharField(max_length=32, null=True, verbose_name='\u52a0\u89e3\u5bc6\u7c7b\u578b'),
            preserve_default=True,
        ),
    ]
