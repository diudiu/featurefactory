# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2017- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.G
    Date: 2017/2017/2/17
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
        接口：反欺诈服务接口开发指南——3.借贷信息——3.4其他机构查询情况

        计算逻辑：提取原数据的data作为dict1，遍历dict1的所有key，如果其对应的value（类型为dict）不存在或者为None，则删除该键值对；
                  否则遍历 dict1.get(a)的所有key，如果其对应的value（类型为str）不存在或者为None，则删除该键值对 。
                  返回其他机构查询中所有非空的信息。

        输出：其他机构借贷信息
        """

        result = {'pingan_other_loan_infos': StringTypeDefault}

        try:
            if self.data['result'] == 0:
                dict1 = self.data.get('data')
                for a in dict1.keys():
                    if not dict1.get(a):
                        del dict1[a]
                        continue
                    for b in dict1.get(a).keys():
                        if not dict1.get(a).get(b):
                                del dict1.get(a)[b]

                for a in dict1.keys():
                    if not dict1.get(a):
                        del dict1[a]

                result['pingan_other_loan_infos'] = dict1
        except Exception as e:
            logging.error(e.message)
        return result



