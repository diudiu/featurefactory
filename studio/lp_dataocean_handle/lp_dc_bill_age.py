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
        接口名称：人人信
        字段名称：'debit_card_account_age': 借记卡账龄 str

        计算逻辑: 直接从接口提取借记卡账龄,即借记卡使用年限,输出类型为int

        输出:
        特征名称: 'dc_bill_age': 借记卡账龄 int
        """

        result = {
            "dc_bill_age": UnsignedIntTypeDefault,
        }
        try:
            base_data = self.data["result"]["rrx_once_all"]["debit_card_account_age"]
            base_data = int(base_data)
            if str(base_data).isdigit():  # 检验借记卡账龄是否只由数字组成,是则转化为int类型
                base_data = int(base_data)
                result["dc_bill_age"] = base_data

        except Exception as e:
                logging.error(e.message)
        finally:
            return result


