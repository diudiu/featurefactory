# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2017- DIGCREDIT, All Rights Reserved.
    ----------------------------------------------
    Author: S.G
    Date:  2017/02/10
    Change Activity:
"""
import logging

logger = logging.getLogger('apps.common')


class Handle(object):
    def __init__(self, data):
        self.data = data

    def handle(self):
        """
        接口名称：电信号码三元素认证
        字段名称：result          返回结果

        输出：
        特征名称：mobile_identity 电信查询返回结果
        """
        try:
            result = {'mobile_identity': 9999}
            mobile_identity = self.data['result']
            if mobile_identity == '00':
                result['mobile_identity'] = 1
            else:
                result['mobile_identity'] = 0
        except Exception as e:
            logging.error(e.message)

        return result
