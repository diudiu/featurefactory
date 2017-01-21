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

from apps.remote.models import FeatureFieldRel


def load_feature_field_from_xls(file_path):
    rule_base_list = []

    xls = xlrd.open_workbook(file_path)
    sheet1 = xls.sheets()[0]
    for row_num in range(sheet1.nrows):
        if row_num == 0:
            continue
        row = sheet1.row_values(row_num)
        rule_base_info = {
            'id': int(row[0]),
            'feature_name': row[1],
            'raw_field_name': row[2],
            'data_identity': row[3],
        }
        rule_base_list.append(rule_base_info)
    return rule_base_list


def init_feature_field():
    all_rule_base = load_feature_field_from_xls('feature_field_rel.xlsx')
    for rule_base in all_rule_base:
        if FeatureFieldRel.objects.filter(
                feature_name=rule_base['feature_name'],
                raw_field_name=rule_base['raw_field_name'],
                data_identity=rule_base['data_identity'],
        ).count() > 0:
            continue
        else:
            ffr = FeatureFieldRel(
                id=rule_base['id'],
                feature_name=rule_base['feature_name'],
                raw_field_name=rule_base['raw_field_name'],
                data_identity=rule_base['data_identity'],
            )
            ffr.save()

if __name__ == '__main__':
    init_feature_field()
