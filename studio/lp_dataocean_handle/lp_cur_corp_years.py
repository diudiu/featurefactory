# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2017- DIGCREDIT, All Rights Reserved.
    ----------------------------------------------
    Author: S.G
    Date:  2017/2/8
    Change Activity:
"""

from datetime import datatime


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        接口：企业工商信息查询s(industrial_commercial_s)
        字段：start_business_date      开业日期
        输出：cur_corp_years           现工作单位工作年限（年数）
        """

        result = {'cur_corp_years': 9999}

        try:
            start_business_date = self.data['content']['start_business_date']
            now = datetime.now()
            start = datetime.strptime(start_business_date, '%Y-%m-%d')
            delta = now - start
            years = delta.days/365
            if years <= 1:
                cur_corp_years = 1
            elif 1 < years <= 2:
                cur_corp_years = 2
            elif 2 < years <= 3:
                cur_corp_years = 3
            elif 3 < years <= 4:
                cur_corp_years = 4
            elif 4 < years <= 5:
                cur_corp_years = 5
            elif 5 < years <= 8:
                cur_corp_years = 6
            elif 8 < years <= 10:
                cur_corp_years = 7
            else:
                cur_corp_years = 8
            result['cur_corp_years'] = cur_corp_years
        except Exception:
            # TODO log this error
            return result

        return result



