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
        接口：反欺诈服务接口——3借贷信息——3.4其他机构查询情况

        计算逻辑：取data的所有key组成date_list,遍历date_list，将所有元素转化为int，组成新的列表date_int_list，
                  将新列表的元素按照从大到小顺序排列，遍历data_int_list前六个元素，得到data字典中其对应value(类型为字典)，
                  得到各个新字典的value组成列表orgNums_list，求orgNums_list元素的和作为近六个月其他信贷机构数量。

        输出：其他信贷机构数量（近6个月）
        """

        result = {"pingan_overdue_corp_count": PositiveSignedTypeDefault}
        date_int_list = []
        orgNums_list = [0]

        try:
            date_list = self.data.get('data').keys()
            for x in date_list:
                date_int_list.append(int(x))
            date_int_list.sort(reverse=True)
            for a in range(6):
                orgNums_date = self.data.get('data').get(str(date_int_list[a]))
                if orgNums_date is None:
                    continue
                else:
                    orgNums = orgNums_date.get('orgNums')
                    if orgNums is None:
                        continue
                    else:
                        orgNums_list.append(int(orgNums))

            result['pingan_overdue_corp_count'] = sum(orgNums_list)
        except Exception as e:
            logging.error(e.message)
        finally:
            return result



