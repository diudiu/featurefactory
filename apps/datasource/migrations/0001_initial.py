# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataSourceInfo',
            fields=[
                ('is_delete', models.BooleanField(default=False, verbose_name='\u662f\u5426\u903b\u8f91\u5220\u9664')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4', null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='\u6700\u540e\u4fee\u6539\u65f6\u95f4')),
                ('id', models.AutoField(serialize=False, verbose_name='\u4e3b\u952e', primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name='\u6570\u636e\u6e90\u4e2d\u6587\u540d')),
                ('data_source_identity', models.CharField(default='', max_length=64, verbose_name='\u6570\u636e\u6e90\u6807\u8bc6')),
                ('desc', models.CharField(max_length=512, null=True, verbose_name='\u6570\u636e\u6e90\u63cf\u8ff0', blank=True)),
                ('protocol_type', models.CharField(max_length=15, verbose_name='\u534f\u8bae\u7c7b\u578b', choices=[(b'http', b'http'), (b'https', b'https'), (b'local', b'local')])),
                ('backend_url', models.CharField(max_length=64, verbose_name='\u57df\u540d')),
                ('api_manager', models.CharField(max_length=256, verbose_name='\u83b7\u53d6\u903b\u8f91\u8def\u5f84')),
            ],
            options={
                'db_table': 'fic_data_source_info',
                'verbose_name': '\u6570\u636e\u6e90\u57fa\u672c\u4fe1\u606f\u8868',
                'verbose_name_plural': '\u6570\u636e\u6e90\u57fa\u672c\u4fe1\u606f\u8868',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DsInterfaceInfo',
            fields=[
                ('is_delete', models.BooleanField(default=False, verbose_name='\u662f\u5426\u903b\u8f91\u5220\u9664')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4', null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='\u6700\u540e\u4fee\u6539\u65f6\u95f4')),
                ('id', models.AutoField(serialize=False, verbose_name='\u4e3b\u952e', primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name='\u63a5\u53e3\u540d\u79f0')),
                ('data_identity', models.CharField(max_length=64, verbose_name='\u63a5\u53e3\u6807\u8bc6')),
                ('route', models.CharField(help_text='/api/gateway/', max_length=128, verbose_name='\u8bbf\u95ee\u8def\u7531')),
                ('method', models.CharField(max_length=32, verbose_name='\u8bbf\u95ee\u65b9\u5f0f', choices=[(b'GET', b'GET'), (b'POST', b'POST'), (b'LOCAL', b'LOCAL')])),
                ('comment', models.CharField(max_length=512, null=True, verbose_name='\u63cf\u8ff0', blank=True)),
                ('common_data', models.CharField(max_length=1024, null=True, verbose_name='\u516c\u5171\u53c2\u6570')),
                ('must_data', models.CharField(max_length=1024, verbose_name='\u5fc5\u4f20\u53c2\u6570')),
                ('is_need_token', models.BooleanField(default=False, verbose_name='\u662f\u5426\u9700\u8981access_token')),
                ('is_need_encrypt', models.BooleanField(default=True, verbose_name='\u662f\u5426\u9700\u8981\u52a0\u5bc6')),
                ('is_async', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5f02\u6b65\u8c03\u7528')),
                ('encrypt_type', models.CharField(max_length=32, null=True, verbose_name='\u52a0\u89e3\u5bc6\u7c7b\u578b')),
                ('data_source', models.ForeignKey(verbose_name='\u6570\u636e\u6e90\u914d\u7f6e', to='datasource.DataSourceInfo')),
            ],
            options={
                'db_table': 'fic_interface_info',
                'verbose_name': '\u63a5\u53e3\u8868',
                'verbose_name_plural': '\u63a5\u53e3\u8868',
            },
            bases=(models.Model,),
        ),
    ]
