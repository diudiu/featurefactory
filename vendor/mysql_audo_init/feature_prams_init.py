# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH(Shaohan Niu), All Rights Reserved.
    -----------------------------------------------------------
    Author: S.JunPeng
    Date:  2016/12/26
    Change Activity:

"""

import os
import sys
import xlrd

home_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(home_path)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'featurefactory.settings')

import django
django.setup()

from apps.etl.models import FeaturePrams

# id = models.AutoField(u'主键', primary_key=True)
# feature_name = models.CharField(u'特征字段名', max_length=64)
# pram_field = models.CharField(u'特征计算参数', max_length=64)
# interface_id = models.IntegerField(u'参数来源接口id')
def load_feature_prams_from_xls(file_path):
    feature_prams_list = []

    xls = xlrd.open_workbook(file_path)
    sheet1 = xls.sheets()[0]
    for row_num in range(sheet1.nrows):
        if row_num == 0:
            continue
        row = sheet1.row_values(row_num)
        rule_base_info = {
            'id': int(row[0]),
            'feature_name': row[1],
            'pram_field': row[2],
            'interface_id': int(row[3]),
        }
        feature_prams_list.append(rule_base_info)
    return feature_prams_list


def init_feature_prams():
    feature_prams_list = load_feature_prams_from_xls('feature_prams.xlsx')
    for feature_prams in feature_prams_list:
        fp = FeaturePrams(
            id=feature_prams['id'],
            feature_name=feature_prams['feature_name'],
            pram_field=feature_prams['pram_field'],
            interface_id=feature_prams['interface_id'],
        )
        fp.save()
