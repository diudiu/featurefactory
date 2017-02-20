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

from apps.etl.models import FeatureShuntConf


def load_feature_shunt_from_xls(file_path):
    feature_shunt_list = []

    xls = xlrd.open_workbook(file_path)
    sheet1 = xls.sheets()[0]
    for row_num in range(sheet1.nrows):
        if row_num == 0:
            continue
        row = sheet1.row_values(row_num)
        rule_base_info = {
            'id': int(row[0]),
            'feature_name': row[1],
            'shunt_key': row[2],
            'shunt_type': row[3],
            'shunt_value': row[4],
            'data_identity': row[5],
        }
        feature_shunt_list.append(rule_base_info)
    return feature_shunt_list


def init_feature_field():
    feature_shunt_list = load_feature_shunt_from_xls('feature_shunt.xlsx')
    for feature_shunt in feature_shunt_list:
        if FeatureShuntConf.objects.filter(
                feature_name=feature_shunt['feature_name'],
                data_identity=feature_shunt['data_identity'],
        ).count() > 0:
            continue
        else:
            ffr = FeatureShuntConf(
                id=feature_shunt['id'],
                feature_name=feature_shunt['feature_name'],
                shunt_key=feature_shunt['shunt_key'],
                shunt_type=feature_shunt['shunt_type'],
                shunt_value=feature_shunt['shunt_value'],
                data_identity=feature_shunt['data_identity'],
            )
            ffr.save()

if __name__ == '__main__':
    init_feature_field()
