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

from apps.etl.models import FeatureProcessInfo


def load_feature_field_from_xls(file_path):
    process_base_list = []

    xls = xlrd.open_workbook(file_path)
    sheet1 = xls.sheets()[0]
    for row_num in range(sheet1.nrows):
        if row_num == 0:
            continue
        row = sheet1.row_values(row_num)
        process_base_info = {
            'id': int(row[0]),
            'feature_name': row[1],
            'process_type': row[2],
            'data_identity': row[3],
        }
        process_base_list.append(process_base_info)
    return process_base_list


def init_feature_field():
    process_base_list = load_feature_field_from_xls('feature_process.xlsx')
    for process_base in process_base_list:
        if FeatureProcessInfo.objects.filter(
                feature_name=process_base['feature_name'],
                process_type=process_base['process_type'],
                data_identity=process_base['data_identity'],
        ).count() > 0:
            continue
        else:
            fpi = FeatureProcessInfo(
                id=process_base['id'],
                feature_name=process_base['feature_name'],
                process_type=process_base['process_type'],
                data_identity=process_base['data_identity'],
            )
            fpi.save()

if __name__ == '__main__':
    init_feature_field()
