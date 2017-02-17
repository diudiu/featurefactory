# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2017- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.G
    Date: 2017/02/10
    Change Activity:
"""


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        接口：反欺诈服务接口开发指南——3.借贷信息——3.4其他机构查询情况
        计算逻辑：遍历data_dict的键值对的所有key，如果对应的value为None，则删除这个键值对；
                 遍历data_dict.get(a)的键值对的所有key，如果对应的value为None，则删除这个键值对。
        输出：其他机构借贷信息
        """

        result = {'pingan_other_loan_infos': '9999'}

        try:
            data_dict = self.data.get('data')
            for a in data_dict.keys():  #遍历data_dict的键值对的所有key，如果对应的value为None，则删除这个键值对
                if data_dict.get(a) is None:
                    del data_dict[a]
                    continue  #之前的代码没有continue，导致第一次测试的结果总是异常，但是之后结果都正常输出。
                for b in data_dict.get(a).keys():  #遍历data_dict.get(a)的键值对的所有key，如果对应的value为None，则删除这个键值对
                    if data_dict.get(a).get(b) is None:
                            del data_dict.get(a)[b]
            result['pingan_other_loan_infos'] = dict
        except Exception:
            pass

        return result



