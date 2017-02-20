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
from vendor.utils.defaults import PositiveSignedTypeDefault

class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        接口：反欺诈服务接口——3借贷信息——3.1逾期信息

        计算逻辑：只考虑近六个月的逾期情况，所以只有三种情况M3和M6都有记录；有M3无M6；无M3有M6；无M3无M6。
                  基于各种情况，取各个逾期公司数量组成一个list,并求和作为近六个月逾期公司数量。

        输出：逾期公司数量（近6个月）
        """

        result = {"pingan_overdue_corp_count": PositiveSignedTypeDefault}
        overdue_corp_count_list = [0]
        type_list = ["bankLoan", "bankCredit", "otherLoan", "otherCredit"]

        try:
            M_list = self.data['data']['record'][0]['classification']

            if M_list[0].keys()[0] == "M3":   # 当M_list的第一条记录是M3时，存在两种情况有M3有M6；有M3无M6
                M3 = M_list[0].get('M3')
                for a in type_list:   # 在M3的情况下遍历type_list的四种类型
                    if M3.get(a) is None:
                        continue
                    else:
                        overdue_corp_count = int(M3.get(a).get('orgNums'))   # 取在M3的a类型情况下 的逾期公司数量
                        if overdue_corp_count is None:
                            continue
                        else:
                            overdue_corp_count_list.append(overdue_corp_count)
                if M_list[1].keys()[0] == "M6":  # M_list的第一条记录是M3的前提下，第二条记录是M6，即有M3有M6
                    M6 = M_list[1].get('M6')
                    for a in type_list:
                        if M6.get(a) is None:
                            continue
                        else:
                            overdue_corp_count = int(M6.get(a).get('orgNums'))
                            if overdue_corp_count is None:
                                continue
                            else:
                                overdue_corp_count_list.append(overdue_corp_count)
            elif M_list[0].keys()[0] == "M6":   # M_list的第一条记录是M6，即无M3有M6
                M6 = M_list[0].get('M6')
                for a in type_list:
                    if M6.get(a) is None:
                        continue
                    else:
                        overdue_corp_count = int(M6.get(a).get('orgNums'))
                        if overdue_corp_count is None:

                            continue
                        else:
                            overdue_corp_count_list.append(overdue_corp_count)
            else:
                pass
            result['pingan_overdue_corp_count'] = sum(overdue_corp_count_list)
        except Exception as e:
            logging.error(e.message)
        finally:
            return result


