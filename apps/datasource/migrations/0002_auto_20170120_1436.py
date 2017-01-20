# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datasource', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dsinterfaceinfo',
            name='method',
            field=models.CharField(max_length=32, verbose_name='\u8bbf\u95ee\u65b9\u5f0f', choices=[(b'GET', b'GET'), (b'POST', b'POST'), (b'LOCAL', b'LOCAL')]),
            preserve_default=True,
        ),
    ]
