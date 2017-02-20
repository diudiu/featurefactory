# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.G
    Date: 2017/02/10
    Change Activity:
"""


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):
        """接口：反欺诈服务接口——3借贷信息——3.1逾期信息
            输出：最长逾期天数（近6个月）
        """
        result = {"pingan_max_overdue_days": 9999}

        try:
            M_list = self.data['record'][0]['classification']
            overdue_days_list = {}
            M3_bankLoan_max_overdue_days = int(M_list[0].get('M3').get('bankLoan').get('longestDays'))
            overdue_days_list.append(M3_bankLoan_max_overdue_days)
            M3_bankCredit_max_overdue_days = int(M_list[0].get('M3').get('bankCredit').get('longestDays'))
            overdue_days_list.append(M3_bankCredit_max_overdue_days)
            M3_otherLoan_max_overdue_days = int(M_list[0].get('M3').get('otherLoan').get('longestDays'))
            overdue_days_list.append(M3_otherLoan_max_overdue_days)
            M3_otherCredit_max_overdue_days = int(M_list[0].get('M3').get('otherCredit').get('longestDays'))
            overdue_days_list.append(M3_otherCredit_max_overdue_days)
            M6_bankLoan_max_overdue_days = int(M_list[1].get('M6').get('bankLoan').get('longestDays'))
            overdue_days_list.append(M6_bankLoan_max_overdue_days)
            M6_bankCredit_max_overdue_days = int(M_list[1].get('M6').get('bankCredit').get('longestDays'))
            overdue_days_list.append(M6_bankCredit_max_overdue_days)
            M6_otherLoan_max_overdue_days = int(M_list[1].get('M6').get('otherLoan').get('longestDays'))
            overdue_days_list.append(M6_otherLoan_max_overdue_days)
            M6_otherCredit_max_overdue_days = int(M_list[1].get('M6').get('otherCredit').get('longestDays'))
            overdue_days_list.append(M6_otherCredit_max_overdue_days)
            pingan_max_overdue_days = max(overdue_days_list)
            result['pingan_max_overdue_days'] = pingan_max_overdue_days
        except Exception:
            # TODO log this error
            return result

        return result



