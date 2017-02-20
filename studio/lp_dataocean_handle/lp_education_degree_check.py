# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2017- DIGCREDIT, All Rights Reserved.
    ----------------------------------------------
    Author: Z.L
    Date:  2017/02/17
    Change Activity:
"""
from apps.common.cache import feature_global_code
from vendor.utils.analyzer import GenericUtils
from vendor.utils.defaults import PositiveSignedTypeDefault
import logging

logger = logging.getLogger('apps.common')


class Handle(object):
    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        输入:
        接口名称：数据堂学历信息查询接口
        字段名称：degree   学历 str

        计算逻辑:从学历信息查询接口提取'学历'字段,并将学历转化为编码,输出为int

        输出：
        特征名称：degree_code   学信网学历 int
        """

        result = {'education_degree_check': PositiveSignedTypeDefault}

        try:
            degree = self.data['content'].get('degree', None)
            if degree:
                education_degree = degree.get('degree', None)
                code_collection = feature_global_code.get("education_degree_check")   # 提取码值字典
                mapped_value = GenericUtils.get_mapped_value(code_collection, education_degree)  # 匹配学历与字典中的值
                result['education_degree_check'] = mapped_value
                if not mapped_value:   # 若无匹配结果,输出5(代表其他)
                    result['education_degree_check'] = 5

        except Exception as e:
                logging.error(e.message)
        finally:
            return result
