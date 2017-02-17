# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2017- DIGCREDIT, All Rights Reserved.
    ----------------------------------------------
    Author: Z.L
    Date:  2017/02/17
    Change Activity:
"""
from vendor.utils.defaults import StringTypeDefault
import logging

logger = logging.getLogger('apps.common')


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        输入:
        接口名称：education_review_s 数据堂学历信息查询接口
        字段名称：college 院校名称 string

        计算逻辑: 从学历信息查询接口提取院校名称并输出,输出为string

        输出：
        特征名称：graduate_college_check 学信网查得院校 string
        """

        result = {'graduate_college_check': StringTypeDefault}

        try:
            college_name = self.data['content']['degree'].get('college', None)
            if college_name and isinstance(college_name, basestring):  # 判断院校名称是否为非空字符串
                result['graduate_college_check'] = college_name

        except Exception as e:
                logging.error(e.message)
        finally:
            return result
