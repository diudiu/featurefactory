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

from apps.common.models import CityCodeField


def load_city_code_from_xls(file_path):
    data_source_info_list = []

    xls = xlrd.open_workbook(file_path)
    sheet1 = xls.sheets()[0]
    for row_num in range(sheet1.nrows):
        if row_num == 0:
            continue
        row = sheet1.row_values(row_num)
        city_code = str(int(row[1]))
        if row[4] == 0.0:
            father_tip = '0'
        else:
            father_tip = '1'
        try:
            father_code = str(int(row[5]))
        except Exception:
            father_code = ''
        if row[7]:
            level = int(row[7])
        else:
            level = None
        data_source_info = {
            'id': int(row[0]),
            'city_code': city_code,
            'city_name_cn': row[2],
            'city_name_en': row[3],
            'father_tip': father_tip,
            'father_code': father_code,
            'seouri': row[6],
            'abbreviation': row[2],
            'city_level': level
        }
        data_source_info_list.append(data_source_info)
    return data_source_info_list


def init_city_code():
    all_city_code_base = load_city_code_from_xls('city_code.xlsx')
    for city_code in all_city_code_base:
        cc = CityCodeField(
            city_name_cn=city_code['city_name_cn'],
            city_name_en=city_code['city_name_en'],
            father_tip=city_code['father_tip'],
            father_code=city_code['father_code'],
            city_code=city_code['city_code'],
            seouri=city_code['seouri'],
            abbreviation=city_code['abbreviation'],
            id=city_code['id'],
            city_level=city_code['city_level']
        )
        cc.save()


if __name__ == '__main__':
    init_city_code()
