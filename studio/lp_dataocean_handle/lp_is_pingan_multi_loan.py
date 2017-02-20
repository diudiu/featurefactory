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
        接口名称：凭安贷款信息
        字段名称：'result'  int

        计算逻辑: 直接从贷款信息接口提取result值,值为'2'为未命中多头借贷名单,否则为命中,输出为int

        输出:
        特征名称: 'is_pingan_multi_loan' 是否命中多头借贷名单 int
        """

        result = {'is_pingan_multi_loan': UnsignedIntTypeDefault}
        try:
            base_data = self.data["result"]
            if base_data == "2":
                result['is_pingan_multi_loan'] = 0  # 若接口result值返回为'2',返回未命中
            else:
                result['is_pingan_multi_loan'] = 1

        except Exception as e:
                logging.error(e.message)
        finally:
            return result

