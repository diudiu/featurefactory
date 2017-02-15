# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2017- DIGCREDIT, All Rights Reserved.
    ----------------------------------------------
    Author: S.G
    Date:  2017/02/10
    Change Activity:
"""


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):
        """
        接口名称：猎聘
        字段名称：work_exp_form       工作信息
                 industry            公司行业名称
                 work_end            工作经历结束时间

        输出：
        特征名称：last_industry_code  上一份工作行业code
        """

        result = {'last_industry_code': 9999}

        try:
            work_exp_form = self.data['work_exp_form']
            if not isinstance(work_exp_form, list):
                return result
            work_end_list = []
            for work_exp in work_exp_form:
                work_end = work_exp.get('work_end', None)
                if not isinstance(work_end, (str, int)):
                    return result
                else:
                    work_end_list.append(int(work_end))
            if len(work_end_list) >= 2:
                last_work_end = sorted(work_end_list)[-2]
                last_woek_end_index = work_end_list.index(last_work_end)
                last_industry_code_dic['last_industry_code'] = work_exp_form[
                    last_woek_end_index].get('industry', None)
            else:
                result['last_industry_code'] = 9999
        except Exception:
            # TODO log this error
            return result

        return result

        return result