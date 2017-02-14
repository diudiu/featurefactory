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
        接口：法院失信被执行人查询As（court_shixin_a_s）
        输出：is_cur_corp_shixin     现工作单位是否为失信被执行
        """

        result = {'is_cur_corp_shixin': 9999}

        if self.data['result'] == "00":
            result['is_cur_corp_shixin'] = 1
        else:
            result['is_cur_corp_shixin'] = 0

        return result



