# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etl', '0023_auto_20170329_1610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='featurecardtype',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='featurecardtype',
            name='is_delete',
        ),
        migrations.RemoveField(
            model_name='featurecardtype',
            name='updated_on',
        ),
        migrations.RemoveField(
            model_name='featureruletype',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='featureruletype',
            name='is_delete',
        ),
        migrations.RemoveField(
            model_name='featureruletype',
            name='updated_on',
        ),
        migrations.RemoveField(
            model_name='featuretype',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='featuretype',
            name='is_delete',
        ),
        migrations.RemoveField(
            model_name='featuretype',
            name='updated_on',
        ),
    ]
