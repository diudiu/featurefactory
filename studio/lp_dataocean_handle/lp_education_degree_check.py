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

from apps.common.cache import feature_global_code
from vendor.utils.analyzer import GenericUtils
from vendor.utils.defaults import PositiveSignedTypeDefault

logger = logging.getLogger('apps.common')


class Handle(object):
    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        接口名称：数据堂学历信息查询接口
        字段名称：degree                     学历code
        输出：
        特征名称：education_degree_check                学历
        """

        result = {'education_degree_check': PositiveSignedTypeDefault}
        try:
            # code_collection = feature_global_code.get("education_degree_check")  # 传入的参数是特征名称
            # feature_value = u"博士"  # 这个需要自己实际从self.data中获取
            # mapped_value = GenericUtils.get_mapped_value(code_collection, feature_value)
            degree = self.data['content'].get('degree', None)
            if degree:
                education_degree = degree.get('degree', None)
                degree_map = {
                    '博士后': 5, '博士': 10, 'MBA/EMBA': 20,
                    '硕士': 30, '本科': 40, '大专': 50,
                    '中专': 60, '中技': 70, '高中': 80, '初中': 90}
                for d, v in degree_map.items():
                    if d in education_degree:
                        result['education_degree_check'] = v
        except Exception as e:
            logging.error(e.message)

        return result
