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
        网贷黑名单
        data_identity: net_black_a_s
        :return:
        """
        try:
            result = {
                'is_net_black': False
            }
            tip = self.data.get('result', None)
            if not tip:
                raise MyException(message='get (result) fail')

            if self.data['result'] == u'00':
                result['is_net_black'] = True
        except MyException as e:
            logging.error(e.message)
        except Exception as e:
            logging.error(e.message)
        finally:
            return result
