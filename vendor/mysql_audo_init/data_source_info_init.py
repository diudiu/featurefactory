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

from apps.datasource.models import DataSourceInfo


def load_data_source_from_xls(file_path):
    data_source_info_list = []

    xls = xlrd.open_workbook(file_path)
    sheet1 = xls.sheets()[0]
    for row_num in range(sheet1.nrows):
        if row_num == 0:
            continue
        row = sheet1.row_values(row_num)
        data_source_info = {
            'id': int(row[0]),
            'name': row[1],
            'data_source_identity': row[2],
            'desc': row[3],
            'protocol_type': row[4],
            'backend_url': row[5],
        }
        data_source_info_list.append(data_source_info)
    return data_source_info_list


def init_data_source():
    all_data_source_base = load_data_source_from_xls('data_source_info.xlsx')
    for data_source in all_data_source_base:
        dsi = DataSourceInfo(
            id=data_source['id'],
            name=data_source['name'],
            data_source_identity=data_source['data_source_identity'],
            desc=data_source['desc'],
            protocol_type=data_source['protocol_type'],
            backend_url=data_source['backend_url'],
        )
        dsi.save()

if __name__ == '__main__':
    init_data_source()
