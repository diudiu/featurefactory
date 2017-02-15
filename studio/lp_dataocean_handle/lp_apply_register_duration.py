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
import logging
from vendor.errors.fecture_error import MyException
logger = logging.getLogger('apps.common')

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
        try:
            result = {
                'apply_register_duration': 999999,
            }
            apply_data = self.data["apply_data"]["application_on"][:10]
            if not apply_data:
                raise MyException(message='get (label) fail')
            if not isinstance(apply_data, basestring):
                raise MyException(message='get (label) fail')
            apply_data = datetime.strptime(apply_data, "%Y-%m-%d")
            register_data = self.data["portrait_data"]["registration_on"][:10]
            if not register_data:
                raise MyException(message='get (label) fail')
            if not isinstance(register_data, basestring):
                raise MyException(message='get (label) fail')
            register_data = datetime.strptime(register_data, "%Y-%m-%d")
            register_time = datetime(register_data.year, register_data.month, register_data.day)
            apply_time = datetime(apply_data.year, apply_data.month, apply_data.day)
            apply_register = (apply_time - register_time).days/30.0
            result['apply_register_duration'] = apply_register
        except MyException as e:
                logging.error(e.message)
        except Exception as e:
                logging.error(e.message)
        finally:
            return result
