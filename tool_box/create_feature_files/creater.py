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
import xlrd

DIR_NAME = 'lp_dataocean_handle'


def load_feature_name_from_xls(file_path):

    xls = xlrd.open_workbook(file_path)
    sheet1 = xls.sheets()[0]
    rule_base_list = sheet1.col_values(0)

    return rule_base_list


def init_feature_field():
    file_list = os.getcwd()
    if DIR_NAME not in file_list:
        os.mkdir(DIR_NAME)

    doc = get_document()
    feature_name_list = load_feature_name_from_xls('feature_name.xlsx')
    for feature_name in feature_name_list:
        file_name = 'lp_dataocean_handle/' + 'lp_' + feature_name + '.py'
        file_handle = open(file_name, 'w+')
        kkk = doc % (feature_name.encode('utf-8'))
        file_handle.write(kkk)
        file_handle.close()


def get_document():
    return open('conf.bat', 'rb').read()


if __name__ == '__main__':
    init_feature_field()
