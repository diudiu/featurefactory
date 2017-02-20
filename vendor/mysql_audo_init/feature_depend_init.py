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

from apps.etl.models import FeatureRelevanceConf


def load_feature_depend_from_xls(file_path):
    feature_depend_list = []

    xls = xlrd.open_workbook(file_path)
    sheet1 = xls.sheets()[0]
    for row_num in range(sheet1.nrows):
        if row_num == 0:
            continue
        row = sheet1.row_values(row_num)
        rule_base_info = {
            'id': int(row[0]),
            'feature_name': row[1],
            'depend_feature': row[2],
            'data_identity': row[3],
        }
        feature_depend_list.append(rule_base_info)
    return feature_depend_list


def init_feature_field():
    feature_depend_list = load_feature_depend_from_xls('feature_depend.xlsx')
    for feature_depend in feature_depend_list:
        if FeatureRelevanceConf.objects.filter(
                feature_name=feature_depend['feature_name'],
                data_identity=feature_depend['data_identity'],
        ).count() > 0:
            continue
        else:
            ffr = FeatureRelevanceConf(
                id=feature_depend['id'],
                feature_name=feature_depend['feature_name'],
                depend_feature=feature_depend['depend_feature'],
                data_identity=feature_depend['data_identity'],
            )
            ffr.save()

if __name__ == '__main__':
    init_feature_field()
