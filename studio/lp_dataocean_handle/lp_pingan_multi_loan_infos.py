# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: ZL
    Date:  2017/01/24
    Change Activity:
"""
import logging

from vendor.errors.fecture_error import MyException

logger = logging.getLogger('apps.common')


class Handle(object):
    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        接口名称：贷款信息

        输出:
        特征名称:
        'pingan_multi_loan_infos': 多头借贷信息
        """
        try:
            result = {
                'pingan_multi_loan_infos': 9999,
            }
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
                        if any(j.values()):
                            tmp.append(j)

                result['pingan_multi_loan_infos'] = tmp

        except Exception as e:
            logging.info(e.message)
        finally:
            return result



