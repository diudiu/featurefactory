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
        接口名称：贷款信息

        计算逻辑: 贷款信息接口返回信息包括按月汇总的银行机构及非银机构发生的贷款信息,
                 提取贷款信息列表,将其中为空的部分删掉

        输出:
        特征名称:
        'pingan_multi_loan_infos': 多头借贷信息
        """
        result = {'pingan_multi_loan_infos': ListTypeDefault}
        try:

            if self.data.get('result', 0) == 0:
                records = self.data["data"]["record"]
                for record in records:
                    base_data = record.get("classification", [])
                    for data in base_data:
                        for in_data in data.keys():
                            time_org = data[in_data]
                            if not time_org or not isinstance(time_org, dict):
                                continue
                            for other_bank_data in time_org.keys():
                                if not time_org[other_bank_data]:
                                    del time_org[other_bank_data]
                                else:
                                    for detail_data in time_org[other_bank_data].keys():
                                        if not time_org[other_bank_data][detail_data]:
                                            del time_org[other_bank_data][detail_data]
                                            if not time_org[other_bank_data]:
                                                del time_org[other_bank_data]
                tmp = []
                for i in records:
                    base_data = i['classification']
                    for j in base_data:
                        if any(j.values()):  # 把非空的元素添加到tmp列表里, 空值去掉
                            tmp.append(j)

                result['pingan_multi_loan_infos'] = tmp

        except Exception as e:
            logging.error(e.message)

        return result



