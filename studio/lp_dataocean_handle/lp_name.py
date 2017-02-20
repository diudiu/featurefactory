# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: ZL
    Date:  2017/01/18
    Change Activity:

    data = {
    "product_code": "890wefjf320if0i302f0j3f0f",
    "apply_id": "APPLY20161011111111890934",
    "callback": "http://10.20.1.110/api/credit/result/",
    "name": "张三",
    "card_id": "411402198002039872",
    "mobile": "18989821092",
    "longitudu": 23.45678,
    "latitude": 145.23342,
    "contacts": 30,
    "application_on": "2017-02-01 12:20:10",
}
"""
import logging

from vendor.utils.defaults import *

logger = logging.getLogger('apps.common')


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        接口名称：猎聘申请信息上传接口
        字段名称：
        'name': 姓名

        输出:
        特征名称:
        'name': 姓名 str
        """
        result = {'name': StringTypeDefault}
        try:
            base_data = self.data.get("name", '')
            if base_data and isinstance(base_data, basestring):
                result['name'] = base_data
        except Exception as e:
            logging.error(e.message)
        return result


