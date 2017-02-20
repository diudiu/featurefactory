# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2013- DIGCREDIT, All Rights Reserved.
    -----------------------------------------------------------
    Author: Z.L
    Date:  2017/02/17
    Change Activity:
"""
from datetime import datetime
from vendor.utils.defaults import PositiveSignedFloatTypeDefault

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

        计算逻辑: 从申请信息上传接口提取贷款申请时间,从预授信接口提取用户注册时间,计算二者时间差
                 输出单位为月, 类型为float保留两位小数

        输出:
        特征名称: 'apply_register_duration'  注册时间长度  float
        """

        result = {'apply_register_duration': PositiveSignedFloatTypeDefault}
        try:
            apply_date = self.data["apply_data"]["application_on"][:10]  # 时间只提取年月日
            register_date = self.data["portrait_data"]["registration_on"][:10]
            apply_date = datetime.strptime(apply_date, "%Y-%m-%d")  # 做成配置文件
            register_date = datetime.strptime(register_date, "%Y-%m-%d")

            apply_register = (apply_date - register_date).days/30.0  # 计算时间差
            apply_register = round(apply_register, 2)
            result['apply_register_duration'] = apply_register

        except Exception as e:
                logging.error(e.message)
        finally:
            return result

