# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.Junpeng
    Date: 2017/01/18
    Change Activity:
"""
from vendor.utils.defaults import UnsignedIntTypeDefault
from apps.common.models import CityCodeField
import logging

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
        result = {
                "mobile_area_city_level": UnsignedIntTypeDefault,
            }
        try:
            if self.data['result'] == u'00':
                mobile_area = self.data['content']['mobile_area']
                city = mobile_area.encode('utf-8')
                if ('市' in city) or ('盟' in city) or ('州' in city and len(city) > 6):
                    city = city[:-3]
                ccf = CityCodeField.objects.filter(
                    city_name_cn=city,
                    is_delete=False
                )
                if ccf:
                    level = ccf[0].city_level
                    if level:
                        result['mobile_area_city_level'] = int(level)
        except Exception as e:
            logging.error(e.message)
        return result
