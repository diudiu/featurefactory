# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.JunPeng
    Date:  2016/12/26
    Change Activity:
"""
import logging
import json

from vendor.utils.constant import cons
from procuratorate.lp_judger import Judger

logger = logging.getLogger('apps.etl')


class DataClean(object):

    def __init__(self, original_data, clean_style):
        self.origin_data = original_data
        self.clean_style = clean_style

    def worked(self):
        if self.clean_style & cons.LP_DATAOCEAN:
            return self._data_ocean_clean()

        if self.clean_style & cons.LP_91_CREDIT:
            return self._91_credit_clean()

        if self.clean_style & cons.LP_PINGAN_CREDIT:
            return self._pingan_credit_clean()

        if self.clean_style & (cons.LP_CC_CREDIT | cons.LP_CC_CAR_CREDIT):
            return self._cc_credit_clean()

        if not self.clean_style:
            return self.origin_data

    def _data_ocean_clean(self):
        temp_data = Judger.get_value(self.origin_data, '$.res_data.res_data')
        if not temp_data or temp_data == '{}':
            logger.error(
                'Unavailable data from %s :\n%s' %
                (cons.SOURCE_TYPE_MESSAGE[self.clean_style], self.origin_data)
            )
            return {}
        # TODO temp_data may is unicode string

        temp_data = json.loads(temp_data)
        return temp_data

    def _91_credit_clean(self):
        temp_data = Judger.get_value(self.origin_data, '$.res_data')
        if not temp_data or temp_data == '{}':
            logger.error(
                'Unavailable data from %s :\n%s' %
                (cons.SOURCE_TYPE_MESSAGE[self.clean_style], self.origin_data)
            )
            return {}
        return temp_data

    def _pingan_credit_clean(self):
        temp_data = Judger.get_value(self.origin_data, '$.res_data.data')
        if not temp_data or temp_data == '{}':
            logger.error(
                'Unavailable data from %s :\n%s' %
                (cons.SOURCE_TYPE_MESSAGE[self.clean_style], self.origin_data)
            )
            return {}
        return temp_data

    def _cc_credit_clean(self):
        temp_data = Judger.get_value(self.origin_data, '$.res_data')
        if not temp_data or temp_data == '{}':
            logger.error(
                'Unavailable data from %s :\n%s' %
                (cons.SOURCE_TYPE_MESSAGE[self.clean_style], self.origin_data)
            )
            return {}
        return temp_data

    def test_worked(self):
        if self.clean_style & cons.LP_DATAOCEAN:
            return {
                'staaaaaaaaaaaatus': u'00',
                'messssssssssssage': '',
                'content': {
                    'consttttttion': '水瓶座',
                    'aggggggggggge': 10,
                    'home_addresss': '江西 - 九江',
                    'sexxxxxxxxxxx': '男',
                },
            }

        if self.clean_style & cons.LP_91_CREDIT:
            return {"data": "test_data"}

        if self.clean_style & cons.LP_PINGAN_CREDIT:
            return {"data": "test_data"}

        if self.clean_style & (cons.LP_CC_CREDIT | cons.LP_CC_CAR_CREDIT):
            return {"data": "test_data"}

        if not self.clean_style:
            return self.origin_data
