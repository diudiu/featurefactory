# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.Junpeng
    Date:  2017/01/18
    Change Activity:
"""
import logging

from vendor.utils.defaults import *
from apps.common.models import CityCodeField

logger = logging.getLogger('apps.common')


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):
        """
        目前无code码存储格式,只返回了城市名称

        接口名称：
        'geo_location': 经纬度获取地址信息
        字段名称：
        'city': 城市名 str

        输出:
        特征名称:
        'gps_city_code': GPS定位城市 str
        """
        result = {
            'gps_city_code': StringTypeDefault,
        }
        try:
            if self.data['result'] == '00':
                base_data = self.data["content"]["result"]["addressComponent"]["city"]
                if base_data and isinstance(base_data, basestring):
                    city = base_data.encode('utf-8')
                    if ('市' in city) or ('盟' in city) or ('州' in city and len(city) > 6):
                        city = city[:-3]
                    ccf = CityCodeField.objects.filter(
                        city_name_cn=city,
                        is_delete=False
                    )
                    if ccf:
                        result['gps_city_code'] = ccf[0].city_code
        except Exception as e:
            logging.error(e.message)

        return result
