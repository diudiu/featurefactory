# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2013- DIGCREDIT, All Rights Reserved.
    -----------------------------------------------------------
    Author: Z.L
    Date:  2017/02/17
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
from vendor.utils.defaults import StringTypeDefault
import logging

logger = logging.getLogger('apps.common')


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        输入:
        接口名称：猎聘申请信息上传接口
        字段名称：'name': 姓名

        计算逻辑: 从猎聘申请信息上传接口提取姓名并输出,输出类型为string

        输出:
        特征名称: 'name': 姓名 str
        """
        result = {'name': StringTypeDefault}

        try:
            base_data = self.data.get("name", '')
            if base_data and isinstance(base_data, basestring):  # 判断姓名是否为非空字符串
                result['name'] = base_data

        except Exception as e:
            logging.error(e.message)
        return result


