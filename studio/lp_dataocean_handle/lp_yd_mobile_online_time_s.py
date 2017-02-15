# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.G
    Date: 2017/01/18
    Change Activity:
"""
# TODO
import logging
from featurefactory.vendor.errors.fecture_error import MyException
logger = logging.getLogger('apps.common')

class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):
        """
        接口：移动号码在网时长查询s(yd_mobile_online_time_s)
        输出：移动手机号在网时长
        :return:
        """
        try:
            result = {"online_time": '9999'}
            tip = self.data.get('result', None)
            if not tip:
                raise MyException(message='get (result) fail')
            if self.data['result'] == u'00':
                online_time = self.data['content']['online_time']
                if online_time in ["(0,3)", "[3,6)"]:
                    online_time = "00"
                elif online_time in "[6,12)":
                    online_time = "11"
                elif online_time in ["[12,18)", "[18,24]"]:
                    online_time = "22"
                elif online_time in ["(24,+)"]:
                    online_time = "33"
                else:
                    online_time = "-1"
                result['online_time'] = online_time
        except MyException as e:
            logging.error(e.message)
        except Exception as e:
            logging.error(e.message)
        finally:
            return result



