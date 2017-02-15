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
from vendor.errors.fecture_error import MyException
logger = logging.getLogger('apps.common')

class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):
        """
        接口：手机号码归属地查询(mobile_locale)
        输出：手机号码归属地
        :return:
        """
        try:
            result = {
             "mobile_area": "",
            }
            tip = self.data.get('result', None)
            if not tip:
                raise MyException(message='get (result) fail')
            if self.data['result'] == u'00':
                mobile_area = self.data['content']['mobile_area']
            else:
                mobile_area = "NONE"
            result['mobile_area'] = mobile_area
        except MyException as e:
            logging.error(e.message)
        except Exception as e:
            logging.error(e.message)
        finally:
            return result
