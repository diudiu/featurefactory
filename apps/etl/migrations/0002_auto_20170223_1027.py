# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etl', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeatureProcess',
            fields=[
                ('is_delete', models.BooleanField(default=False, verbose_name='\u662f\u5426\u903b\u8f91\u5220\u9664')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4', null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='\u6700\u540e\u4fee\u6539\u65f6\u95f4')),
                ('id', models.AutoField(serialize=False, verbose_name='\u4e3b\u952e', primary_key=True)),
                ('feature_name', models.CharField(max_length=64, verbose_name='\u7279\u5f81\u5b57\u6bb5\u540d')),
                ('feature_data_type', models.CharField(max_length=64, verbose_name='\u7279\u5f81\u5b57\u6bb5\u7c7b\u578b')),
                ('default_value', models.CharField(max_length=64, verbose_name='\u7279\u5f81\u7f3a\u7701\u503c')),
                ('json_path_list', models.CharField(max_length=2048, verbose_name='\u7279\u5f81\u5904\u7406\u6d41\u7a0b')),
                ('map_and_filter_chain', models.CharField(max_length=1024, null=True, verbose_name='\u7279\u5f81\u5904\u7406map\u94fe')),
                ('reduce_chain', models.CharField(max_length=1024, verbose_name='\u7279\u5f81\u5904\u7406reduce\u94fe')),
            ],
            options={
                'db_table': 'fic_feature_process_info',
                'verbose_name': '\u7279\u5f81\u8ba1\u7b97\u65b9\u5f0f\u914d\u7f6e\u8868',
                'verbose_name_plural': '\u7279\u5f81\u8ba1\u7b97\u65b9\u5f0f\u914d\u7f6e\u8868',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='featureconf',
            name='data_origin_type',
            field=models.IntegerField(null=True, verbose_name='\u6570\u636e\u6e90\u6807\u8bb0'),
            preserve_default=True,
        ),
    ]
