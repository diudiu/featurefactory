# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2017- DIGCREDIT, All Rights Reserved.
    ----------------------------------------------
    Author: Sun Fei
    Date:  2017/1/18
    Change Activity:
"""
import logging
from vendor.errors.fecture_error import MyException
logger = logging.getLogger('apps.common')


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):
        """
        接口名称：电信号码三元素认证
        字段名称：result          返回结果

        输出：
        特征名称：mobile_identity 电信查询返回结果
        """
        try:
            mobile_identity_dic = {'mobile_identity': 9999}  # 9999：异常
            mobile_identity = self.data.get('result', None)
            if not mobile_identity:
                raise MyException(message='get (mobile_identity) fail')
            if mobile_identity == '00':
                mobile_identity_dic['mobile_identity'] = 1
            else:
                mobile_identity_dic['mobile_identity'] = 0
        except MyException as e:
            logging.error(e.message)
        except Exception as e:
            logging.error(e.message)
        finally:
            return mobile_identity_dic
