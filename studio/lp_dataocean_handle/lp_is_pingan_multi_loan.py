# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2013- DIGCREDIT, All Rights Reserved.
    -----------------------------------------------------------
    Author: Z.L
    Date:  2017/02/17
    Change Activity:
"""
import logging

from vendor.utils.defaults import *

logger = logging.getLogger('apps.common')


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        输入:
        接口名称：凭安贷款信息
        字段名称：'result'  int

        计算逻辑: 直接从贷款信息接口提取result值,值为'0'且返回贷款信息列表不为空则为命中多头借贷名单,否则为未命中,输出为int

        输出:
        特征名称: 'is_pingan_multi_loan' 是否命中多头借贷名单 int
        """

        result = {'is_pingan_multi_loan': BooleanTypeDefault}
        try:
            if self.data["result"] == 0:
                record = self.data.get("data", {}).get("record", [])
                for i in record:
                    if i.get("classification"):  # 且返回结果不为空,返commit 回命中
                        result['is_pingan_multi_loan'] = 1
                        break
                    else:
                        result['is_pingan_multi_loan'] = 0

        except Exception as e:
            import traceback
            traceback.print_exc()
            logging.error(e.message)

        return result

