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
logger = logging.getLogger('apps.common')
from vendor.utils.defaults import StringTypeDefault

class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        接口：反欺诈服务接口开发指南——3.借贷信息——3.4其他机构查询情况

        计算逻辑：提取原数据的data作为dict1，遍历dict1的所有key，如果其对应的value（类型为dict）不存在或者为None，则删除该键值对；
                  否则遍历 dict1.get(a)的所有key，如果如果其对应的value（类型为str）不存在或者为None，则删除该键值对 。
                  返回其他机构查询中所有非空的信息。

        输出：其他机构借贷信息
        """

        result = {'pingan_other_loan_infos': StringTypeDefault}

        try:
            dict1 = self.data.get('data')
            for a in dict1.keys():
                if not dict1.get(a) or dict1.get(a) is None:
                    del dict1[a]
                    continue
                for b in dict1.get(a).keys():
                    if not dict1.get(a).get(b) or dict1.get(a).get(b) is None:
                            del dict1.get(a)[b]

            result['pingan_other_loan_infos'] = dict1
        except Exception as e:
            logging.error(e.message)
        finally:
            return result



