# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2017- DIGCREDIT, All Rights Reserved.
    ----------------------------------------------
    Author: S.Junpeng
    Date:  2017/02/17
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
        输入:
        接口名称：数据堂学历信息查询接口
        字段名称：address 住址

        计算逻辑:企业工商信息查询s接口返回值取address字段 提取城市名称关键字匹配查询数据库得到相应城市等级

        输出：
        特征名称：company_addr_city_level 企业所在城市等级 int
        """

        result = {'company_addr_city_level': UnsignedIntTypeDefault}

        try:
            if self.data['result'] == '00':
                content = self.data['content']
                if not content:
                    raise
                address = content.get('address', None)
                if not address:
                    raise
                city_name = ''
                for tip in ['市', '盟', '州']:
                    if tip in address:
                        index = address.find(tip)
                        city_name = address[:index]
                        city_name = city_name.encode('utf-8')
                        if len(city_name) == 3:
                            city_name += '州'
                        break
                if city_name:
                    ccf = CityCodeField.objects.filter(
                        city_name_cn=city_name,
                        is_delete=False
                    )
                    if ccf:
                        company_addr_city_level = ccf[0].city_level
                        if company_addr_city_level:
                            result['company_addr_city_level'] = int(company_addr_city_level)

        except Exception as e:
            logging.error(e.message)
        finally:
            return result
