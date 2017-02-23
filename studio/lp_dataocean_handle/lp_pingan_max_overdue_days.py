# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.G
    Date: 2017/2017/2/17
    Change Activity:
"""

import logging

from vendor.utils.defaults import PositiveSignedTypeDefault

logger = logging.getLogger('apps.common')


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        接口：反欺诈服务接口——3借贷信息——3.1逾期信息

        计算逻辑：只考虑近六个月的逾期情况，所以只有四种情况M3和M6都有记录；有M3无M6；无M3有M6；无M3无M6。
                  基于各种情况，取各个最长逾期天数组成一个list,并取最大值作为近六个月最长逾期天数。
                  （当M_list的第一条记录是M3时，存在两种情况有M3有M6；有M3无M6。在M3的情况下遍历type_list的四种类型，
                  取在M3的各类型情况下的逾期天数，如果该逾期天数为None,则进行下一次循环，否则将逾期天数加入overdue_days_list）

        输出：最长逾期天数（近6个月）
        """

        result = {"pingan_max_overdue_days": PositiveSignedTypeDefault}
        overdue_days_list = [0]
        type_list = ["bankLoan", "bankCredit", "otherLoan", "otherCredit"]

        try:
            M_list = self.data['data']['record'][0]['classification']

            if M_list[0].keys()[0] == "M3":  # 当M_list的第一条记录是M3时，存在两种情况有M3有M6；有M3无M6
                M3 = M_list[0].get('M3')
                for a in type_list:   # 在M3的情况下遍历type_list的四种类型
                    if M3.get(a) is None:
                        continue
                    else:
                        overdue_days = M3.get(a).get('longestDays')   # 取在M3的a类型情况下的逾期天数
                        if overdue_days is None:   # 如果该逾期天数为None,则进行下一次循环
                            continue
                        else:
                            overdue_days_list.append(int(overdue_days))  # 将逾期天数组成列表
                if M_list[1].keys()[0] == "M6":  # M_list的第一条记录是M3的前提下，第二条记录是M6，即有M3有M6
                    M6 = M_list[1].get('M6')
                    for a in type_list:
                        if M6.get(a) is None:
                            continue
                        else:
                            overdue_days = M6.get(a).get('longestDays')
                            if overdue_days is None:
                                continue
                            else:
                                overdue_days_list.append(int(overdue_days))
            elif M_list[0].keys()[0] == "M6":    # M_list的第一条记录是M6，即无M3有M6
                M6 = M_list[0].get('M6')
                for a in type_list:
                    if M6.get(a) is None:
                        continue
                    else:
                        overdue_days = M6.get(a).get('longestDays')
                        if overdue_days is None:
                            continue
                        else:
                            overdue_days_list.append(int(overdue_days))
            else:
                pass
            result['pingan_max_overdue_days'] = max(overdue_days_list)
        except Exception as e:
            logging.error(e.message)
        finally:
            return result



