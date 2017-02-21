# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: LJY
    Date:  2017/01/23
    Change Activity:

    data = {
    "result": "00" ,
    "result_message" : "检测通过或查询有记录",
    "content" : {
    "constellation" : "水瓶座",
    "age": 24,
    "home_address" : "江西-九江",
    "sex" : "男"
    },
    }
"""
import logging

from vendor.utils.defaults import PositiveSignedTypeDefault

logger = logging.getLogger('apps.common')


class Handle(object):
    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        接口名称：个人基本信息查询
        字段名称：
        gender 性别

        输出:
        特征名称: 性别
        字段名称:
        'gender': 性别
        """
        result = {'gender': PositiveSignedTypeDefault}
        try:
            if self.data['result'] == '00':
                base_data = self.data['content']['sex']
                if base_data and isinstance(base_data, basestring):
                    if '男' in base_data:
                        result['gender'] = 0
                    if '女' in base_data:
                        result['gender'] = 1
        except Exception as e:
            logging.error(e.message)
        return result
