# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2017- DIGCREDIT, All Rights Reserved.
    ----------------------------------------------
    Author: S.G
    Date:  2017/2/8
    Change Activity:
"""

import numpy as np


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        接口：猎聘
        字段：work_exp_form       工作信息
              comp_name           公司名称
              work_end            工作经历结束时间

        输出：cur_company    当前工作单位
        """

        result = {'cur_company': '9999'}

        try:
            work_exp_form = self.data['work_exp_form']
            if not isinstance(work_exp_form, list):
                return result
            work_end_list = []
            for work_exp in work_exp_form:
                work_end = work_exp.get('work_end', None)
                if not isinstance(work_end, (basestring, int)):
                    return result
                else:
                    work_end_list.append(int(work_end))
            result['cur_company'] = work_exp_form[
                np.argmax(work_end_list)].get('comp_name', None)
        except Exception:
            # TODO log this error
            return result

        return result
