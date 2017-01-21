# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: ZL
    Date:  2017/01/18
    Change Activity:
"""
# TODO


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
            'gps_city_code': 999999,
        }
        try:
            base_data = self.data["content"]["result"]["addressComponent"]["city"]
        except Exception as e:
            # TODO log this error
            return result
        if not base_data or not isinstance(base_data, str):
            return result

        result['gps_city_code'] = base_data
        return result
