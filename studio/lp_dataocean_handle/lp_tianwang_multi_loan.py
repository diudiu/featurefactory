# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.Junpeng
    Date:  2017/01/20
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
        天网多头借贷
        data_identity: tianwang_multi_loan
        :return:
        """
        try:
            result = {
                'is_netsky_longloan': False
            }
            tip = self.data.get('result', None)
            if not tip:
                raise MyException(message='get (result) fail')
            if self.data['result'] == u'00':
                result['is_netsky_longloan'] = True
        except MyException as e:
            logging.error(e.message)
        except Exception as e:
            logging.error(e.message)
        finally:
            return result
