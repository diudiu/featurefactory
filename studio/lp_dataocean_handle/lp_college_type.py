# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2017- DIGCREDIT, All Rights Reserved.
    ----------------------------------------------
    Author: Z.L
    Date:  2017/02/14
    Change Activity:
"""


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        输入:
        接口名称：数据堂学历信息查询接口
        字段名称：school_nature 学校性质  degree 学历

        计算逻辑:根据学校性质判断是211还是985,如果学校性质匹配
                无结果,则根据学历判断是本科还是专科,输出类型为int

        输出：
        特征名称：college_type 毕业/在读学校类型 int
        """

        result = {'college_type': '9999'}

        try:
            college_nature = self.data['content']['college'].get('school_nature', None)
            degree = self.data['content']['degree'].get('degree', None)

            nature_code = {
                '专科': 1,
                '本科': 2,
                '211': 3,
                '985': 4,
            }
            # 判断是否是211 985
            for nature in nature_code.keys():
                if nature in college_nature:
                    result['college_type'] = nature_code[nature]
            # 无匹配结果,判断学历
            if result['college_type'] == '9999':
                for nature in nature_code.keys():
                    if nature in degree:
                        result['college_type'] = nature_code[nature]
            return result

        except Exception:
            # TODO log this error
            return result
