# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2017- DIGCREDIT, All Rights Reserved.
    ----------------------------------------------
    Author: S.G
    Date:  2017/2/8
    Change Activity:
"""


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        接口：企业工商信息查询s(industrial_commercial_s)
        字段：staff_count              职工人数
        输出：cur_employee_number      现工作单位规模（人数）
        """

        result = {'cur_employee_number': 9999}

        try:
            staff_count = int(self.data['content']['staff_count'])
            if staff_count < 20:
                cur_employee_number = 1
            elif 20 <= staff_count < 100:
                cur_employee_number = 2
            elif 100 <= staff_count < 500:
                cur_employee_number = 3
            elif 500 <= staff_count < 1000:
                cur_employee_number = 4
            elif 1000 <= staff_count < 10000:
                cur_employee_number = 5
            else:
                cur_employee_number = 6
            result['cur_employee_number'] = cur_employee_number
        except Exception:
            # TODO log this error
            return result

        return result



