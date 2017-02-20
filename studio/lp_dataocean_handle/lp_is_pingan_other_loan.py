# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2017- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.G
    Date: 2017/2/17
    Change Activity:
"""

import logging
logger = logging.getLogger('apps.common')
from vendor.utils.defaults import UnsignedIntTypeDefault

class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):

        """

        """

        result = {"is_pingan_other_loan": UnsignedIntTypeDefault}

        try:
            if self.data['result'] == 0:
                result['is_pingan_other_loan'] = 1
            else:
                result['is_pingan_other_loan'] = 0
        except Exception as e:
            logging.error(e.message)
        finally:
            return result



