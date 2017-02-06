# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: ZL
    Date:  2017/01/24
    Change Activity:
"""


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

        result = {
            'pingan_multi_loan_infos': 999999,
        }
        try:
            base_data = self.data["data"]["record"][0]["classification"]
        except Exception as e:
            # TODO log this error
            return result
        if not base_data or not isinstance(base_data, list):
            return result

        for data in base_data:
            for in_data in data.keys():
                try:
                    time_org = data[in_data]
                except Exception as e:
                    # TODO log this error
                    pass
                if not time_org or not isinstance(time_org, dict):
                    del time_org
                for other_bank_data in time_org.keys():
                    if not time_org[other_bank_data]:
                        del time_org[other_bank_data]
                    else:
                        for detail_data in time_org[other_bank_data].keys():
                            if not time_org[other_bank_data][detail_data]:
                                del time_org[other_bank_data][detail_data]

        result['pingan_multi_loan_infos'] = base_data
        return result
