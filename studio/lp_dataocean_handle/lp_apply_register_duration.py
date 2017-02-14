# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: ZL
    Date:  2017/01/18
    Change Activity:
"""
from datetime import datetime
import time


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        接口名称：
        猎聘申请信息上传接口
        猎聘预授信接口
        字段名称：
        'registration_on': 用户注册时间 str
        'application_on': 贷款申请时间 str

        输出:
        特征名称:
        'apply_register_duration': 注册时间长度 float
        """

        result = {
            'apply_register_duration': 9999,
        }
        try:
            apply_data = self.data["apply_data"]["application_on"]
            register_data = self.data["portrait_data"]["registration_on"]
            if not apply_data or not isinstance(apply_data, str):
                return result
            if not register_data or not isinstance(register_data, str):
                return result

            apply_data = apply_data[0:10]
            register_data = register_data[0:10]
            apply_data = datetime.strptime(apply_data, "%Y-%m-%d")
            register_data = datetime.strptime(register_data, "%Y-%m-%d")

            register_time = datetime(register_data.year, register_data.month, register_data.day)
            apply_time = datetime(apply_data.year, apply_data.month, apply_data.day)
            apply_register = (apply_time - register_time).days/30.0
            apply_register = round(apply_register, 2)

            result['apply_register_duration'] = apply_register

            return result
        except Exception as e:
            # TODO log this error
            return result

