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

from apps.etl.models import PreFieldInfo


def load_field_info_from_xls(file_path):
    field_info_conf_list = []

    xls = xlrd.open_workbook(file_path)
    sheet1 = xls.sheets()[0]
    for row_num in range(sheet1.nrows):
        if row_num == 0:
            continue
        row = sheet1.row_values(row_num)
        feature_conf = {
            'id': int(row[0]),
            'field_name': row[1],
            'field_name_cn': row[2],
            'source': row[3],
            'path': row[4],
        }
        field_info_conf_list.append(feature_conf)
    return field_info_conf_list


def init_feature_field():
    all_feature_conf = load_field_info_from_xls('pre_field_info.xlsx')
    for feature_conf in all_feature_conf:
        if PreFieldInfo.objects.filter(
                field_name=feature_conf['field_name'],
        ).count() > 0:
            continue
        else:
            pfi = PreFieldInfo(
                id=feature_conf['id'],
                field_name=feature_conf['field_name'],
                field_name_cn=feature_conf['field_name_cn'],
                source=feature_conf['source'],
                path=feature_conf['path'],
            )
            pfi.save()

if __name__ == '__main__':
    init_feature_field()
