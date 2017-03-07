# -*- coding: utf-8 -*-
import unittest
import xlrd
import xlwt
import os
from studio.fecture_comment_handle.featrue_process import FeatureProcess


file_path = os.path.join(os.path.dirname(__file__), 'test_case.xlsx')
result_path = os.path.join(os.path.dirname(__file__), 'resultcase.xlsx')


def read_excle(file_path):
    wb = xlwt.Workbook()
    ws = wb.add_sheet('A Test Sheet')
    pattern_yellow = xlwt.Pattern()
    ws.write(0, 0, 'feature_name')
    ws.write(0, 1, 'expect_result')
    ws.write(0, 2, 'test_result')
    book = xlrd.open_workbook(file_path)
    book_sheet = book.sheet_by_index(0)
    nrows = book_sheet.nrows
    for i in range(1, nrows):
        feature_name = book_sheet.cell(i, 0).value
        datas = eval(book_sheet.cell(i, 1).value)
        expect_result = book_sheet.cell(i, 2).value
        expect_res = expect_result.encode("utf-8")
        fecture_obj = FeatureProcess(feature_name, datas)
        result = fecture_obj.run()
        result.values()
        try:
            ws.write(i, 0, feature_name)
            ws.write(i, 1, expect_result)
            if result.values() == [expect_res]:
                ws.write(i, 2, u'测试通过')
            else:
                ws.write(i, 3, u'测试失败')
                pattern_yellow.pattern_fore_colour = 5
        except Exception:
            pass
        finally:
            wb.save(result_path)

        print feature_name, result.values(), expect_result
if __name__ == '__main__':
    read_excle(file_path)
