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
        接口名称：猎聘预授信接口
        字段名称：edu_exp_form     教育信息
                  degree          学历code

        计算逻辑: 提取猎聘学历信息并转化为编码, 编码需要与学信网编码一致, 输出类型为int

        输出：
        特征名称：education_degree_code      学历
        """

        result = {'education_degree_code': PositiveSignedTypeDefault}

        try:
            edu_exp_form = self.data['edu_exp_form']
            if edu_exp_form and isinstance(edu_exp_form, list):  # 判断学历信息是非空的list
                degree_list = []
                for edu_exp in edu_exp_form:
                    degree = edu_exp.get('degree', None)   # 提取学历,提取失败则返回空
                    degree_list.append(degree)

                code_collection = feature_global_code.get("education_degree_code")
                for degree_data in code_collection:
                    mapped_value = GenericUtils.get_mapped_value(code_collection, degree_data)
                    if mapped_value:   # 匹配学历编码,若匹配成功则将学历列表中code值转化为对应int型code
                        degree_list = [mapped_value if x == degree_data else x for x in degree_list]
                degree_list = [5 if isinstance(x, str) else x for x in degree_list]  # 将学历列表中未匹配成功的全部替换为5
                result['education_degree_code'] = min(degree_list)  # 取学历列表的最小值,即最高学历编码

        except Exception as e:
                logging.error(e.message)
        finally:
            return result
