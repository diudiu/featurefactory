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
        接口：反欺诈服务接口——3借贷信息——3.1逾期信息
        输出：逾期公司数量（近6个月）
        """

        result = {"pingan_overdue_corp_count": 9999}

        try:
            M_list = self.data['record'][0]['classification']
            M3_bankLoan_overdue_corp_count = M_list[0].get('M3').get('bankLoan').get('orgNums')
            if M3_bankLoan_overdue_corp_count is None:
                M3_bankLoan_overdue_corp_count = 0
            M3_bankCredit_overdue_corp_count = M_list[0].get('M3').get('bankCredit').get('orgNums')
            if M3_bankCredit_overdue_corp_count is None:
                M3_bankCredit_overdue_corp_count = 0
            M3_otherLoan_overdue_corp_count = M_list[0].get('M3').get('otherLoan').get('orgNums')
            if M3_otherLoan_overdue_corp_count is None:
                M3_otherLoan_overdue_corp_count = 0
            M3_otherCredit_overdue_corp_count = M_list[0].get('M3').get('otherCredit').get('orgNums')
            if M3_otherCredit_overdue_corp_count is None:
                M3_otherCredit_overdue_corp_count = 0
            M6_bankLoan_overdue_corp_count = M_list[1].get('M6').get('bankLoan').get('orgNums')
            if M6_bankLoan_overdue_corp_count is None:
                M6_bankLoan_overdue_corp_count = 0
            M6_bankCredit_overdue_corp_count = M_list[1].get('M6').get('bankCredit').get('orgNums')
            if M6_bankCredit_overdue_corp_count is None:
                M6_bankCredit_overdue_corp_count = 0
            M6_otherLoan_overdue_corp_count = M_list[1].get('M6').get('otherLoan').get('orgNums')
            if M6_otherLoan_overdue_corp_count is None:
                M6_otherLoan_overdue_corp_count = 0
            M6_otherCredit_overdue_corp_count = M_list[1].get('M6').get('otherCredit').get('orgNums')
            if M6_otherCredit_overdue_corp_count is None:
                M6_otherCredit_overdue_corp_count = 0
            pingan_ovredue_corp_count = M3_bankLoan_overdue_corp_count \
                                   + M3_bankCredit_overdue_corp_count \
                                   + M3_otherLoan_overdue_corp_count \
                                   + M3_otherCredit_overdue_corp_count \
                                   + M6_bankLoan_overdue_corp_count \
                                   + M6_bankCredit_overdue_corp_count \
                                   + M6_otherLoan_overdue_corp_count \
                                   + M6_otherCredit_overdue_corp_count
            result['pingan_overdue_corp_count'] = pingan_ovredue_corp_count
        except Exception:
            return result

        return result


