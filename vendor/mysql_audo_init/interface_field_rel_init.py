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

from apps.datasource.models import InterfaceFieldRel


def load_interface_field_from_xls(file_path):
    rule_base_list = []

    xls = xlrd.open_workbook(file_path)
    sheet1 = xls.sheets()[0]
    for row_num in range(sheet1.nrows):
        if row_num == 0:
            continue
        row = sheet1.row_values(row_num)
        rule_base_info = {
            'id': int(row[0]),
            'data_identity': row[1],
            'raw_field_name': row[2],
        }
        rule_base_list.append(rule_base_info)
    return rule_base_list


def init_interface_field():
    interface_field_base = load_interface_field_from_xls('interface_field_rel.xlsx')
    for interface_field in interface_field_base:
        if InterfaceFieldRel.objects.filter(
                data_identity=interface_field['data_identity'],
                raw_field_name=interface_field['raw_field_name'],
        ).count() > 0:
            continue
        else:
            ffr = InterfaceFieldRel(
                id=interface_field['id'],
                data_identity=interface_field['data_identity'],
                raw_field_name=interface_field['raw_field_name'],
            )
            ffr.save()

if __name__ == '__main__':
    init_interface_field()
