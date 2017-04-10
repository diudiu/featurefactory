# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etl', '0024_auto_20170410_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='featurecardtype',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u903b\u8f91\u5220\u9664'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='featureruletype',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u903b\u8f91\u5220\u9664'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='featuretype',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u903b\u8f91\u5220\u9664'),
            preserve_default=True,
        ),
    ]
