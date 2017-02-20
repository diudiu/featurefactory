# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2013- DIGCREDIT, All Rights Reserved.
    -----------------------------------------------------------
    Author: Z.L
    Date:  2017/02/17
    Change Activity:
"""
from vendor.utils.defaults import UnsignedIntTypeDefault
import logging

logger = logging.getLogger('apps.common')


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        输入:
        接口名称：人人信征信服务接口
        字段名称：'credit_cards_num': 信用卡张数 str

        计算逻辑: 从人人信征信服务接口提取'信用卡张数'并输出, 输出类型为int

        输出:
        特征名称: 'creditcard_count': 信用卡张数 int
        """

        result = {"creditcard_count": UnsignedIntTypeDefault}
        try:
            base_data = self.data["result"]["rrx_once_all"]["credit_cards_num"]
            if str(base_data).isdigit():  # 检验信用卡张数是否只由数字组成,是则转化为int类型
                base_data = int(base_data)
                result["creditcard_count"] = base_data

        except Exception as e:
                logging.error(e.message)
        finally:
            return result

