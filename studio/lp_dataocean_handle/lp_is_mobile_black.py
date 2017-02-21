# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2017- DIGCREDIT, All Rights Reserved.
    ----------------------------------------------
    Author: S.G
    Date:  2017/02/10
    Change Activity:
"""
import logging

from vendor.utils.defaults import *

logger = logging.getLogger('apps.common')


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        接口名称：凭安反欺诈服务接口
        字段名称：result              查询结果
                 grayscale           染黑度

        输出：
        特征名称：is_mobile_black     手机号是否染黑
        """

        result = {'is_mobile_black': BooleanTypeDefault}
        try:
            is_mobile_black = self.data.get('result')
            grayscale = self.data.get('data', {}).get('grayscale')
            if is_mobile_black == 0:
                result['is_mobile_black'] = 1
            elif is_mobile_black == 2 and grayscale == {}:
                result['is_mobile_black'] = 0
        except Exception as e:
            logging.error(e.message)
        return result
