# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etl', '0007_auto_20170324_1115'),
    ]

    operations = [
        migrations.CreateModel(
            name='FuncLibSource',
            fields=[
                ('is_delete', models.BooleanField(default=False, verbose_name='\u662f\u5426\u903b\u8f91\u5220\u9664')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4', null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='\u6700\u540e\u4fee\u6539\u65f6\u95f4')),
                ('func_name', models.CharField(max_length=64, serialize=False, verbose_name='\u51fd\u6570\u540d', primary_key=True)),
                ('func_desc', models.CharField(max_length=64, verbose_name='\u51fd\u6570\u63cf\u8ff0')),
                ('func_type', models.CharField(max_length=10, verbose_name='\u51fd\u6570\u7c7b\u578b', choices=[(b'M', b'map'), (b'F', b'filter'), (b'R', b'reduce'), (b'A', b'assert')])),
            ],
            options={
                'db_table': 'fic_func_lib',
                'verbose_name': '\u51fd\u6570\u5e93\u914d\u7f6e\u8868',
                'verbose_name_plural': '\u51fd\u6570\u5e93\u914d\u7f6e\u8868',
            },
            bases=(models.Model,),
        ),
    ]
