# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2017- DIGCREDIT, All Rights Reserved.
    ----------------------------------------------
    Author: Z.L
    Date:  2017/02/17
    Change Activity:
"""
from vendor.utils.defaults import PositiveSignedTypeDefault
from apps.common.cache import feature_global_code
from vendor.utils.analyzer import GenericUtils
import logging

logger = logging.getLogger('apps.common')


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        输入:
        接口名称：数据堂学历信息查询接口
        字段名称：school_nature 学校性质  degree 学历

        计算逻辑:从学历信息接口提取学校性质和学历,根据学校性质判断是211还是985,
                如果学校性质匹配无结果,则根据学历判断是本科还是专科,输出类型为int

        输出：
        特征名称：college_type 毕业/在读学校类型 int
        """

        result = {'college_type': PositiveSignedTypeDefault}

        try:
            college_nature = self.data['content']['college'].get('school_nature', None)
            degree = self.data['content']['degree'].get('degree', None)

            code_collection = feature_global_code.get("college_type")
            mapped_value = GenericUtils.get_mapped_value(code_collection, college_nature)  # 匹配是否是211 985
            if not mapped_value:  # 若不是211 985,则匹配学历是本科还是专科
                mapped_value = GenericUtils.get_mapped_value(code_collection, degree)
            result['college_type'] = mapped_value

        except Exception as e:
                logging.error(e.message)
        finally:
            return result
