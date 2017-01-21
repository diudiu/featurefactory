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

from apps.datasource.models import DsInterfaceInfo
from apps.datasource.models import DataSourceInfo


def load_interface_info_from_xls(file_path):
    interface_base_list = []

    xls = xlrd.open_workbook(file_path)
    sheet1 = xls.sheets()[0]
    for row_num in range(sheet1.nrows):
        if row_num == 0:
            continue
        row = sheet1.row_values(row_num)
        rule_base_info = {
            'id': int(row[0]),
            'name': row[1],
            'data_identity': row[2],
            'data_source': DataSourceInfo.objects.filter(id=int(row[3]))[0],
            'route': row[4],
            'method': row[5],
            'comment': row[6],
            'common_data': row[7],
            'must_data': row[8],
            'is_need_token': int(row[9]),
            'is_need_encrypt': int(row[10]),
            'is_async': int(row[11]),
            'encrypt_type': row[12],
        }
        interface_base_list.append(rule_base_info)
    return interface_base_list


def init_interface_info():
    interface_base_list = load_interface_info_from_xls('interface_info.xlsx')
    for interface_base in interface_base_list:
        if DsInterfaceInfo.objects.filter(data_identity=interface_base['data_identity']).count() > 0:
            continue
        else:
            dsi = DsInterfaceInfo(
                id=interface_base['id'],
                name=interface_base['name'],
                data_identity=interface_base['data_identity'],
                data_source=interface_base['data_source'],
                route=interface_base['route'],
                method=interface_base['method'],
                comment=interface_base['comment'],
                common_data=interface_base['common_data'],
                must_data=interface_base['must_data'],
                is_need_token=interface_base['is_need_token'],
                is_need_encrypt=interface_base['is_need_encrypt'],
                is_async=interface_base['is_async'],
                encrypt_type=interface_base['encrypt_type'],
            )
            dsi.save()

if __name__ == '__main__':
    init_interface_info()
