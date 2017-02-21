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

from datetime import datetime
from vendor.utils.defaults import PositiveSignedTypeDefault
from apps.common.cache import feature_global_code
from vendor.utils.analyzer import GenericUtils

logger = logging.getLogger('apps.common')


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        接口：企业工商信息查询s(industrial_commercial_s)

        字段：start_business_date      开业日期

        计算逻辑：提取企业的开业日期，并将其转化为datetime格式，然后跟现在时间作差，得到企业已开业天数，
                  除以365.0得到浮点型的企业已开业年数。然后对企业已开业年数进行分段并输出对应code值。

        输出：cur_corp_years           现工作单位年限（年数）
        """

        result = {'cur_corp_years': PositiveSignedTypeDefault}

        try:
            start_business_date = self.data['content']['start_business_date']    # 提取企业的开业日期,得到现在的时间
            now = datetime.now()
            start = datetime.strptime(start_business_date, '%Y-%m-%d')   # 转化为datetime格式
            delta = now - start   # 现在时间作差，得到企业已开业天数
            years = delta.days/365.0   # 除以365.0得到浮点型的企业已开业年数

            code_collection = feature_global_code.get("cur_corp_years")
            mapped_value = GenericUtils.get_mapped_value(code_collection, years)
            result['cur_corp_years'] = mapped_value
        except Exception as e:
            logging.error(e.message)
        finally:
            return result
