# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2017- DIGCREDIT, All Rights Reserved.
    ----------------------------------------------
    Author: S.G
    Date:  2017/2/17
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
        接口：法院失信被执行人查询As（court_shixin_a_s）

        计算逻辑：判断result返回值是否为"00",如果是，则命中其他机构查询名单，返回1；否则认为未命中，返回0。

        输出：is_cur_corp_shixin     现工作单位是否为失信被执行
        """

        result = {'is_cur_corp_shixin': UnsignedIntTypeDefault}

        try:
            if self.data['result'] == "00":
                result['is_cur_corp_shixin'] = 1
            else:
                result['is_cur_corp_shixin'] = 0
        except Exception as e:
            logging.error(e.message)
        finally:
            return result



