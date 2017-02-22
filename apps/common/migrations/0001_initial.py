# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityCodeField',
            fields=[
                ('is_delete', models.BooleanField(default=False, verbose_name='\u662f\u5426\u903b\u8f91\u5220\u9664')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4', null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='\u6700\u540e\u4fee\u6539\u65f6\u95f4')),
                ('id', models.AutoField(serialize=False, verbose_name='\u4e3b\u952e', primary_key=True)),
                ('city_name_cn', models.CharField(max_length=256, verbose_name='\u57ce\u5e02\u4e2d\u6587\u540d')),
                ('city_name_en', models.CharField(max_length=256, verbose_name='\u57ce\u5e02\u82f1\u6587\u540d')),
                ('father_tip', models.CharField(max_length=256, verbose_name='\u7236\u7c7b\u5b50\u7c7b\u6807\u8bc6')),
                ('father_code', models.CharField(max_length=256, null=True, verbose_name='\u7236\u7c7b\u7f16\u7801')),
                ('city_code', models.CharField(max_length=256, verbose_name='\u5730\u533a\u7f16\u7801')),
                ('seouri', models.CharField(max_length=256, verbose_name='')),
                ('abbreviation', models.CharField(max_length=256, null=True, verbose_name='\u7b80\u79f0')),
                ('city_level', models.IntegerField(null=True, verbose_name='\u57ce\u5e02\u7b49\u7ea7')),
            ],
            options={
                'db_table': 'fic_city_code_field',
                'verbose_name': '',
                'verbose_name_plural': '',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FeatureCodeMapping',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_delete', models.BooleanField(default=False, verbose_name='\u662f\u5426\u903b\u8f91\u5220\u9664')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4', null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='\u6700\u540e\u4fee\u6539\u65f6\u95f4')),
                ('feature_name', models.CharField(max_length=128, verbose_name='\u7279\u5f81\u540d\u79f0')),
                ('feature_desc', models.CharField(max_length=128, verbose_name='\u7279\u5f81\u4e2d\u6587\u89e3\u91ca')),
                ('unitary_value', models.CharField(max_length=64, verbose_name='\u53d6\u503c\u57fa\u51c6\u503c')),
                ('dual_value', models.CharField(max_length=64, null=True, verbose_name='\u53d6\u503c\u7684\u6700\u5927\u503c')),
                ('mapped_value', models.IntegerField(verbose_name='\u6620\u5c04\u4e4b\u540e\u7684\u503c')),
                ('value_type', models.CharField(max_length=20, verbose_name='\u7279\u5f81\u539f\u6765\u503c\u7684\u7c7b\u578b', choices=[(b'string', b'string'), (b'int', b'int'), (b'float', b'float')])),
            ],
            options={
                'db_table': 'fic_feature_code_mapping',
                'verbose_name': '\u7279\u5f81\u7801\u503c\u5bf9\u5e94\u8868',
                'verbose_name_plural': '\u7279\u5f81\u7801\u503c\u5bf9\u5e94\u8868',
            },
            bases=(models.Model,),
        ),
    ]
