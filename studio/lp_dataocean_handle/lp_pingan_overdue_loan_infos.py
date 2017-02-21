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
        接口：反欺诈服务接口开发指南——3.借贷信息——3.1逾期信息

        计算逻辑：提取classification的信息作为classification_list，遍历classification_list的所有元素（类型为dict），遍历
                  classification_list[x]的所有key，遍历其对应得的value（类型为dict）的所有key，如果其对应的value(类型为dict)，
                  则删除该键值对；否则其对应得的value（类型为dict）的所有key，如果其对应的value(类型为dict)，则删除该键值对。

        输出：逾期信息
        """

        result = {"pingan_overdue_loan_infos":  StringTypeDefault}

        try:
            classification_list = self.data.get('data').get('record')[0].get('classification')

            for x in range(len(classification_list)):
                for a in classification_list[x].keys():
                    for b in classification_list[x].get(a).keys():
                        if not classification_list[x].get(a).get(b) or classification_list[x].get(a).get(b) is None:
                            del classification_list[x].get(a)[b]
                        else:
                            for c in classification_list[x].get(a).get(b).keys():
                                if not classification_list[x].get(a).get(b).get(c) or classification_list[x].get(a).get(b).get(c) is None:
                                    del classification_list[x].get(a).get(b)[c]

            result['pingan_overdue_loan_infos'] = classification_list
        except Exception as e:
            logging.error(e.message)
        finally:
            return result



