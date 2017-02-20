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
from vendor.utils.defaults import PositiveSignedTypeDefault
from apps.common.cache import feature_global_code
from vendor.utils.analyzer import GenericUtils

class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        接口：企业工商信息查询s(industrial_commercial_s)

        字段：staff_count              职工人数

        计算逻辑：提取staff_count，对其进行分段并返回对应code值

        输出：cur_employee_number      现工作单位规模（人数）
        """

        result = {'cur_employee_number': PositiveSignedTypeDefault}

        try:
            staff_count = int(self.data['content']['staff_count'])

            code_collection = feature_global_code.get("cur_employee_number")
            mapped_value = GenericUtils.get_mapped_value(code_collection, staff_count)
            result['cur_employee_number'] = mapped_value
        except Exception as e:
            logging.error(e.message)
        finally:
            return result



