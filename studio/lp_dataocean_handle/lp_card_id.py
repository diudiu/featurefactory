# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2013- DIGCREDIT, All Rights Reserved.
    -----------------------------------------------------------
    Author: Z.L
    Date:  2017/02/17
    Change Activity:
"""
from vendor.utils.defaults import StringTypeDefault
import logging

logger = logging.getLogger('apps.common')


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        输入:
        接口名称：猎聘申请信息上传接口
        字段名称：card_id 身份证号 str

        计算逻辑: 直接从申请信息上传接口提取身份证号并输出, 类型为string

        输出:
        特征名称: 身份证号
        字段名称: 'card_id': 身份证号 string
        """

        result = {'card_id': StringTypeDefault}
        try:
            base_data = self.data['card_id']
            if base_data and isinstance(base_data, basestring):  # 判断身份证号不为空且为字符串格式
                result['card_id'] = base_data

        except Exception as e:
                logging.error(e.message)
        finally:
            return result

