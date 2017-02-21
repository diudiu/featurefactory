# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2017- DIGCREDIT, All Rights Reserved.
    ----------------------------------------------
    Author: Z.L
    Date:  2017/02/17
    Change Activity:
"""
from vendor.utils.defaults import *
import logging

logger = logging.getLogger('apps.common')


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        输入:
        接口名称：education_review_s 数据堂学历信息查询接口
        字段名称：education_approach 学习形式

        计算逻辑: 从学历信息查询接口提取学习形式,如果学习形式为全日制,则为统招,输出为1;否则为非统招,输出为0

        输出：
        特征名称：is_recruitment 是否统招 int
        """

        result = {'is_recruitment': BooleanTypeDefault}

        try:
            education_info = self.data['content']['degree'].get('education_approach', None)
            if education_info and isinstance(education_info, basestring):  # 判断学习形式是否为非空字符串
                if '全日制' in education_info:
                    result['is_recruitment'] = 1  # 学习形式包含全日制则为统招,返回1,否则返回0
                else:
                    result['is_recruitment'] = 0

        except Exception as e:
                logging.error(e.message)
        finally:
            return result
