# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeatureConf',
            fields=[
                ('is_delete', models.BooleanField(default=False, verbose_name='\u662f\u5426\u903b\u8f91\u5220\u9664')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4', null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='\u6700\u540e\u4fee\u6539\u65f6\u95f4')),
                ('id', models.AutoField(serialize=False, verbose_name='\u4e3b\u952e', primary_key=True)),
                ('feature_name', models.CharField(max_length=64, verbose_name='\u7279\u5f81\u5b57\u6bb5\u540d')),
                ('feature_name_cn', models.CharField(max_length=128, verbose_name='\u7279\u5f81\u4e2d\u6587\u540d')),
                ('data_identity', models.CharField(max_length=512, verbose_name='\u539f\u59cb\u6570\u636e\u6807\u8bc6')),
                ('collect_type', models.CharField(max_length=64, null=True, verbose_name='\u6570\u636e\u83b7\u53d6\u65b9\u5f0f')),
                ('raw_field_name', models.CharField(max_length=2048, verbose_name='\u53c2\u6570\u5b57\u6bb5\u540d')),
            ],
            options={
                'db_table': 'fic_feature_common_conf',
                'verbose_name': '\u4e00\u822c\u7279\u5f81\u5904\u7406\u903b\u8f91\u914d\u7f6e\u8868',
                'verbose_name_plural': '\u4e00\u822c\u7279\u5f81\u5904\u7406\u903b\u8f91\u914d\u7f6e\u8868',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FeatureRelevanceConf',
            fields=[
                ('is_delete', models.BooleanField(default=False, verbose_name='\u662f\u5426\u903b\u8f91\u5220\u9664')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4', null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='\u6700\u540e\u4fee\u6539\u65f6\u95f4')),
                ('id', models.AutoField(serialize=False, verbose_name='\u4e3b\u952e', primary_key=True)),
                ('feature_name', models.CharField(max_length=64, verbose_name='\u7279\u5f81\u5b57\u6bb5\u540d')),
                ('depend_feature', models.CharField(max_length=64, null=True, verbose_name='\u6b64\u7279\u5f81\u4f9d\u8d56\u7684\u5176\u4ed6\u7279\u5f81\u540d')),
                ('data_identity', models.CharField(max_length=64, verbose_name='')),
            ],
            options={
                'db_table': 'fic_feature_relevance_conf',
                'verbose_name': '\u4f9d\u8d56\u5173\u7cfb\u5904\u7406\u903b\u8f91\u914d\u7f6e\u8868',
                'verbose_name_plural': '\u4f9d\u8d56\u5173\u7cfb\u5904\u7406\u903b\u8f91\u914d\u7f6e\u8868',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FeatureShuntConf',
            fields=[
                ('is_delete', models.BooleanField(default=False, verbose_name='\u662f\u5426\u903b\u8f91\u5220\u9664')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4', null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='\u6700\u540e\u4fee\u6539\u65f6\u95f4')),
                ('id', models.AutoField(serialize=False, verbose_name='\u4e3b\u952e', primary_key=True)),
                ('feature_name', models.CharField(max_length=64, verbose_name='\u7279\u5f81\u5b57\u6bb5\u540d')),
                ('shunt_key', models.CharField(max_length=64, verbose_name='\u5206\u6d41\u4f9d\u636e\u5b57\u6bb5\u540d\u79f0')),
                ('shunt_type', models.CharField(max_length=256, verbose_name='\u5206\u6d41\u903b\u8f91\u540d')),
                ('shunt_value', models.CharField(max_length=256, verbose_name='\u5206\u6d41\u6bd4\u8f83\u503c')),
                ('data_identity', models.CharField(max_length=64, verbose_name='\u539f\u59cb\u6570\u636e\u6807\u8bc6')),
            ],
            options={
                'db_table': 'fic_feature_shunt_conf',
                'verbose_name': '\u5206\u6d41\u5904\u7406\u903b\u8f91\u914d\u7f6e\u8868',
                'verbose_name_plural': '\u5206\u6d41\u5904\u7406\u903b\u8f91\u914d\u7f6e\u8868',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PreFieldInfo',
            fields=[
                ('is_delete', models.BooleanField(default=False, verbose_name='\u662f\u5426\u903b\u8f91\u5220\u9664')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4', null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='\u6700\u540e\u4fee\u6539\u65f6\u95f4')),
                ('id', models.AutoField(serialize=False, verbose_name='\u4e3b\u952e', primary_key=True)),
                ('field_name', models.CharField(max_length=64, verbose_name='\u5b57\u6bb5\u540d\u79f0')),
                ('field_name_cn', models.CharField(max_length=64, verbose_name='\u4e2d\u6587\u540d\u79f0')),
                ('source', models.CharField(max_length=64, verbose_name='\u6570\u636e\u6765\u6e90')),
                ('path', models.CharField(max_length=256, verbose_name='JsonPath\u8def\u5f84')),
            ],
            options={
                'db_table': 'fic_pre_field_info',
                'verbose_name': '\u9884\u5904\u7406\u5b57\u6bb5\u8868',
                'verbose_name_plural': '\u9884\u5904\u7406\u5b57\u6bb5\u8868',
            },
            bases=(models.Model,),
        ),
    ]
