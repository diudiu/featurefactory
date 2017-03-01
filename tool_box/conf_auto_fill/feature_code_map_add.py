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

from apps.common.models import FeatureCodeMapping


def load_feature_map_from_xls(file_path):
    feature_conf_list = []

    xls = xlrd.open_workbook(file_path)
    sheet1 = xls.sheets()[0]
    for row_num in range(sheet1.nrows):
        if row_num == 0:
            continue
        row = sheet1.row_values(row_num)
        feature_conf = {
            'id': int(row[0]),
            'feature_name': row[1],
            'mapped_value': row[2],
            'feature_desc': row[3],
            'unitary_value': row[4],
            'dual_value': row[5],
            'value_type': row[6],
            'arithmetic_type': row[7],
        }
        feature_conf_list.append(feature_conf)
    return feature_conf_list


def init_feature_map_code():
    all_feature_conf = load_feature_map_from_xls('feature_code_map.xlsx')
    for feature_conf in all_feature_conf:
        if FeatureCodeMapping.objects.filter(
                feature_name=feature_conf['feature_name'],
                mapped_value=feature_conf['mapped_value']
        ).count() > 0:
            continue
        else:
            fc = FeatureCodeMapping(
                id=feature_conf['id'],
                feature_name=feature_conf['feature_name'],
                feature_desc=feature_conf['feature_desc'],
                unitary_value=feature_conf['unitary_value'],
                dual_value=feature_conf['dual_value'],
                mapped_value=feature_conf['mapped_value'],
                value_type=feature_conf['value_type'],
                arithmetic_type=feature_conf['arithmetic_type'],
            )
            fc.save()

if __name__ == '__main__':
    init_feature_map_code()
