# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientOverview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_delete', models.BooleanField(default=False, verbose_name='\u662f\u5426\u903b\u8f91\u5220\u9664')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4', null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='\u6700\u540e\u4fee\u6539\u65f6\u95f4')),
                ('client_code', models.CharField(max_length=128, verbose_name='')),
                ('client_id', models.CharField(max_length=128, verbose_name='')),
                ('client_secret', models.CharField(max_length=256, verbose_name='')),
                ('des_key', models.CharField(max_length=128, verbose_name='')),
            ],
            options={
                'db_table': 'fic_client_overview',
                'verbose_name': '',
                'verbose_name_plural': '',
            },
            bases=(models.Model,),
        ),
    ]
