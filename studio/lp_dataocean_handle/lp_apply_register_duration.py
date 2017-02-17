# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2013- DIGCREDIT, All Rights Reserved.
    -----------------------------------------------------------
    Author: Z.L
    Date:  2017/01/18
    Change Activity:
"""
from datetime import datetime

import logging

logger = logging.getLogger('apps.common')


class Handle(object):
    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        输入:
        接口名称：猎聘申请信息上传接口  猎聘预授信接口
        字段名称：'application_on'  贷款申请时间 str
                 'registration_on'  用户注册时间 str

        计算逻辑: 从申请信息上传接口提取贷款申请时间,从预授信接口提取用户注册时间,计算时间差
                 输出单位为月, 类型为float保留两位小数

        输出:
        特征名称: 'apply_register_duration'  注册时间长度  float
        """

        try:
            result = {
                'apply_register_duration': 9999.0,
            }
            apply_data = self.data["apply_data"]["application_on"][:10]  # 时间只提取年月日
            register_data = self.data["portrait_data"]["registration_on"][:10]
            apply_data = datetime.strptime(apply_data, "%Y-%m-%d")
            register_data = datetime.strptime(register_data, "%Y-%m-%d")

            register_time = datetime(register_data.year, register_data.month, register_data.day)
            apply_time = datetime(apply_data.year, apply_data.month, apply_data.day)
            apply_register = (apply_time - register_time).days/30.0  # 计算时间差
            apply_register = round(apply_register, 2)
            result['apply_register_duration'] = apply_register
        except Exception as e:
                logging.error(e.message)
        finally:
            return result

