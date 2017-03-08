# -*- coding: utf-8 -*-
import os
import xlrd

excle_path = os.path.join(os.path.dirname(__file__), 'tp.xlsx')
file_path = os.path.join(os.path.dirname(__file__), 'config zl.py')
txt_path = os.path.join(os.path.dirname(__file__), 'templete.txt')


def create(feature_data, feature_name, feature_default, feature_data_type):
    feature_hand = open(file_path, 'a+')
    res = open(txt_path, 'r').read()
    print res
    feature_hand.write(res % (feature_data, feature_name, feature_default, feature_data_type))
    feature_hand.write('\n')
    feature_hand.write('\n')


def load_feature_conf():
    book = xlrd.open_workbook(excle_path)
    book_sheet = book.sheet_by_index(0)
    nrows = book_sheet.nrows
    feature_hand = open(file_path,'w+')
    feature_hand.write('# -*- coding: utf-8 -*-')
    feature_hand.write('\n\n')
    feature_hand.close()
    for i in range(1, nrows):
        tz_data = book_sheet.cell(i, 0).value
        tz_name = '"' + book_sheet.cell(i, 0).value + '"'
        tz_default = '"' + book_sheet.cell(i, 2).value + '"'
        tz_data_type = '"' + book_sheet.cell(i, 1).value + '"'
        create(tz_data, tz_name, tz_default, tz_data_type)
if __name__ == '__main__':
    load_feature_conf()
