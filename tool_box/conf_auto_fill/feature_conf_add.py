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

from apps.etl.models import FeatureConf


def load_feature_conf_from_xls(file_path):
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
            'feature_name_cn': row[2],
            'data_identity': row[3],
            'collect_type': row[4],
            'raw_field_name': row[5],
        }
        feature_conf_list.append(feature_conf)
    return feature_conf_list


def init_feature_field():
    all_feature_conf = load_feature_conf_from_xls('feature_common_conf.xlsx')
    for feature_conf in all_feature_conf:
        if FeatureConf.objects.filter(
                feature_name=feature_conf['feature_name'],
        ).count() > 0:
            continue
        else:
            fc = FeatureConf(
                id=feature_conf['id'],
                feature_name=feature_conf['feature_name'],
                feature_name_cn=feature_conf['feature_name_cn'],
                data_identity=feature_conf['data_identity'],
                collect_type=feature_conf['collect_type'],
                raw_field_name=feature_conf['raw_field_name'],
            )
            fc.save()

if __name__ == '__main__':
    init_feature_field()
