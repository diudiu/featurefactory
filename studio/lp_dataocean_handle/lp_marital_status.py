# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: ZL
    Date:  2017/01/23
    Change Activity:

    data = {
    "result": "00" ,
    "result_message" : "检测通过或查询有记录",
        'content': {
            'id_card_name': '李..',
            'marital_status': '10',
            'id_card_code': '1306251....',
            'verify': '一致',
            'company': '暂无',
            'nation': '汉族',
            'former_name': '',
            'native_place': '河北省保定市徐水县',
            'birthday': '1988-09-10',
            'birth_place': '河北省保定市徐水县',
            'sex_id': '2',
            'photo': '',
            'education': '大学本科（简称"大学"）',
            'address': '河北省保定市徐水区高林村镇'
        }
    }
"""
import logging
from vendor.utils.defaults import StringTypeDefault

logger = logging.getLogger('apps.common')


class Handle(object):
    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        接口名称：多项身份信息s
        字段名称：
        marital_status 婚姻状况

        输出:
        特征名称: 婚姻状况
        字段名称:
        'marital_status': 婚姻状况
        """
        result = {
            'marital_status': StringTypeDefault,
        }
        try:
            if self.data['result'] == '00':
                base_data = self.data['content']['marital_status']
                if base_data.isdigit():
                    result['marital_status'] = base_data
        except Exception as e:
            logging.error(e.message)
        return result
