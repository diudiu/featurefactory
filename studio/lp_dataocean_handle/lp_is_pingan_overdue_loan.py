# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2017- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.G
    Date: 2017/2/17
    Change Activity:
"""

import logging
logger = logging.getLogger('apps.common')
from vendor.utils.defaults import UnsignedIntTypeDefault

class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        接口：反欺诈服务接口——3借贷信息——3.1逾期信息

        计算逻辑：判断result返回值是否为0,如果是，则命中凭安逾期名单，返回1；否则认为未命中，返回0。

        输出：是否命中凭安逾期名单（近24个月）
        """

        result = {"is_pingan_overdue_loan": UnsignedIntTypeDefault}

        try:
            if self.data['result'] == 0:
                result['is_pingan_overdue_loan'] = 1
            else:
                result['is_pingan_overdue_loan'] = 0
        except Exception as e:
            logging.error(e.message)
        finally:
            return result



