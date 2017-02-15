# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2017- DIGCREDIT, All Rights Reserved.
    ----------------------------------------------
    Author: ZL
    Date:  2017/02/14
    Change Activity:
"""


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        接口名称：数据堂学历信息查询接口
        字段名称：school_nature 学校性质  degree 学历
        输出：
        特征名称：college_type 毕业/在读学校类型
        """

        result = {'college_type': '9999'}

        try:
            college_nature = self.data['content']['college'].get('school_nature', None)
            nature_code = {
                '专科': 1,
                '本科': 2,
                '211': 3,
                '985': 4,
            }
            for nature in nature_code.keys():
                if nature in college_nature:
                    result['college_type'] = nature_code[nature]
            return result

        except Exception:
            # TODO log this error
            return result
