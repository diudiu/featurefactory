# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeatureFieldRel',
            fields=[
                ('is_delete', models.BooleanField(default=False, verbose_name='\u662f\u5426\u903b\u8f91\u5220\u9664')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4', null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='\u6700\u540e\u4fee\u6539\u65f6\u95f4')),
                ('id', models.AutoField(serialize=False, verbose_name='\u4e3b\u952e', primary_key=True)),
                ('feature_name', models.CharField(max_length=64, verbose_name='\u7279\u5f81\u5b57\u6bb5\u540d')),
                ('raw_field_name', models.CharField(max_length=64, verbose_name='\u53c2\u6570\u5b57\u6bb5\u540d')),
            ],
            options={
                'db_table': 'fic_feature_field_rel',
                'verbose_name': '\u7279\u5f81-\u53c2\u6570\u6620\u5c04\u8868',
                'verbose_name_plural': '\u7279\u5f81-\u53c2\u6570\u6620\u5c04\u8868',
            },
            bases=(models.Model,),
        ),
    ]
