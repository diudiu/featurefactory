# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etl', '0004_auto_20170324_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='featureconf',
            name='feature_select_value',
            field=models.CharField(max_length=2048, null=True, verbose_name='\u7279\u5f81\u53ef\u9009\u503c'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='featureconf',
            name='feature_card_type',
            field=models.ForeignKey(db_column=b'feature_card_type', to='etl.FeatureCardType', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='featureconf',
            name='feature_rule_type',
            field=models.ForeignKey(db_column=b'feature_rule_type', to='etl.FeatureRuleType', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='featureconf',
            name='feature_type',
            field=models.ForeignKey(db_column=b'feature_type', to='etl.FeatureType', null=True),
            preserve_default=True,
        ),
    ]
