# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etl', '0003_auto_20170320_1107'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeatureCardType',
            fields=[
                ('is_delete', models.BooleanField(default=False, verbose_name='\u662f\u5426\u903b\u8f91\u5220\u9664')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4', null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='\u6700\u540e\u4fee\u6539\u65f6\u95f4')),
                ('id', models.AutoField(serialize=False, verbose_name='\u4e3b\u952e', primary_key=True)),
                ('feature_type_desc', models.CharField(max_length=2048, verbose_name='\u7279\u5f81\u8bc4\u5206\u5361\u7c7b\u578b\u89e3\u91ca')),
            ],
            options={
                'db_table': 'fic_feature_card_type',
                'verbose_name': '\u7279\u5f81\u8bc4\u5206\u5361\u7c7b\u578b\u914d\u7f6e\u8868',
                'verbose_name_plural': '\u7279\u5f81\u8bc4\u5206\u5361\u7c7b\u578b\u914d\u7f6e\u8868',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FeatureRuleType',
            fields=[
                ('is_delete', models.BooleanField(default=False, verbose_name='\u662f\u5426\u903b\u8f91\u5220\u9664')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4', null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='\u6700\u540e\u4fee\u6539\u65f6\u95f4')),
                ('id', models.AutoField(serialize=False, verbose_name='\u4e3b\u952e', primary_key=True)),
                ('feature_type_desc', models.CharField(max_length=2048, verbose_name='\u7279\u5f81\u89c4\u5219\u7c7b\u578b\u89e3\u91ca')),
            ],
            options={
                'db_table': 'fic_feature_rule_type',
                'verbose_name': '\u7279\u5f81\u89c4\u5219\u7c7b\u578b\u914d\u7f6e\u8868',
                'verbose_name_plural': '\u7279\u5f81\u89c4\u5219\u7c7b\u578b\u914d\u7f6e\u8868',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FeatureType',
            fields=[
                ('is_delete', models.BooleanField(default=False, verbose_name='\u662f\u5426\u903b\u8f91\u5220\u9664')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4', null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='\u6700\u540e\u4fee\u6539\u65f6\u95f4')),
                ('id', models.AutoField(serialize=False, verbose_name='\u4e3b\u952e', primary_key=True)),
                ('feature_type_desc', models.CharField(max_length=2048, verbose_name='\u7279\u5f81\u7c7b\u578b\u89e3\u91ca')),
            ],
            options={
                'db_table': 'fic_feature_type',
                'verbose_name': '\u7279\u5f81\u7c7b\u578b\u914d\u7f6e\u8868',
                'verbose_name_plural': '\u7279\u5f81\u7c7b\u578b\u914d\u7f6e\u8868',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='featureconf',
            name='feature_card_type_desc',
        ),
        migrations.RemoveField(
            model_name='featureconf',
            name='feature_rule_type_desc',
        ),
        migrations.RemoveField(
            model_name='featureconf',
            name='feature_type_desc',
        ),
    ]
