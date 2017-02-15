# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelCoefficientConf',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_delete', models.BooleanField(default=False, verbose_name='\u662f\u5426\u903b\u8f91\u5220\u9664')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4', null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='\u6700\u540e\u4fee\u6539\u65f6\u95f4')),
                ('model_name', models.CharField(max_length=128, verbose_name='\u6a21\u578b\u540d\u79f0')),
                ('coefficient', models.FloatField(default=1.0, verbose_name='\u7cfb\u6570')),
                ('income_interval_min', models.IntegerField(default=0, verbose_name='\u6536\u5165\u533a\u95f4\u6700\u5c0f\u503c')),
                ('income_interval_max', models.IntegerField(default=0, verbose_name='\u6536\u5165\u533a\u95f4\u6700\u5927\u503c')),
                ('computational_formula', models.CharField(default=b'', max_length=512, verbose_name='\u8ba1\u7b97\u516c\u5f0f')),
            ],
            options={
                'db_table': 'pgc_model_coefficient_conf',
                'verbose_name': '\u6388\u4fe1\u6a21\u578b\u7cfb\u6570\u914d\u7f6e\u8868',
                'verbose_name_plural': '\u6388\u4fe1\u6a21\u578b\u7cfb\u6570\u914d\u7f6e\u8868',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ModelFieldOptionWeight',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_delete', models.BooleanField(default=False, verbose_name='\u662f\u5426\u903b\u8f91\u5220\u9664')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4', null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='\u6700\u540e\u4fee\u6539\u65f6\u95f4')),
                ('model_name', models.CharField(max_length=128, verbose_name='\u6a21\u578b\u540d\u79f0')),
                ('field_name', models.CharField(max_length=128, verbose_name='\u5b57\u6bb5\u540d\u79f0')),
                ('field_option_value', models.CharField(default=b'', max_length=20, null=True, verbose_name='\u5b57\u6bb5\u9009\u9879')),
                ('field_option_name', models.CharField(max_length=64, null=True, verbose_name='\u5b57\u6bb5\u9009\u9879\u4e2d\u6587\u540d\u79f0')),
                ('field_option_weight', models.FloatField(default=1.0, null=True, verbose_name='\u5b57\u6bb5\u9009\u9879\u6743\u91cd')),
            ],
            options={
                'db_table': 'pgc_model_field_option_weight',
                'verbose_name': '\u6388\u4fe1\u6a21\u578b\u5b57\u6bb5\u6743\u91cd\u8868',
                'verbose_name_plural': '\u6388\u4fe1\u6a21\u578b\u5b57\u6bb5\u6743\u91cd\u8868',
            },
            bases=(models.Model,),
        ),
    ]
