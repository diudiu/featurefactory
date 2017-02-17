# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2013- DIGCREDIT, All Rights Reserved.
    -----------------------------------------------------------
    Author: Z.L
    Date:  2017/01/18
    Change Activity:
"""


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        输入:
        接口名称：猎聘申请信息上传接口
        字段名称：card_id 身份证号 str

        计算逻辑: 直接从申请信息上传接口提取,类型为string

        输出:
        特征名称: 身份证号
        字段名称: 'card_id': 身份证号 string
        """

        result = {
            'card_id': '9999',
        }
        try:
            base_data = self.data['card_id']
            if not base_data or not isinstance(base_data, basestring):
                return result

            result['card_id'] = base_data

            return result
        except Exception as e:
            # TODO log this error
            return result

