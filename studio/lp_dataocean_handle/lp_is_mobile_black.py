# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2017- DIGCREDIT, All Rights Reserved.
    ----------------------------------------------
    Author: Sun Fei
    Date:  2017/1/20
    Change Activity:
"""


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):
        """
        接口名称：凭安反欺诈服务接口
        字段名称：result              查询结果
                  grayscale           染黑度

        输出：
        特征名称：is_mobile_black     手机号是否染黑
        """

        is_mobile_black_dic = {'is_mobile_black': 9999}  # 9999：异常

        is_mobile_black = self.data.get('result', 9999)  # 9999：异常
        grayscale = self.data.get('grayscale', 9999)

        if is_mobile_black == 0:
            is_mobile_black_dic['is_mobile_black'] = 1
        elif is_mobile_black == 2 and grayscale == {}:
            is_mobile_black_dic['is_mobile_black'] = 0

        return is_mobile_black_dic
