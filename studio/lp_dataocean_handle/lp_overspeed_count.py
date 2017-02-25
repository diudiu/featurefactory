# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: ZL
    Date:  2017/01/24
    Change Activity:
    data = {
        "XXXX1234":
        {
            "result": "00",
            "result_message": "检测通过或查询有记录",
            "content": {
                "license_plate": "渝FC8***",
                "start_time": "201401",
                "end_time": "201412",
                "over_speed_times": 2,
                "over_speed_list": [{
                    "count_month": "201506",
                    "month_times": 2,
                    "section": "北京通州站-河北燕郊站，河北廊坊站-天津蓟县站",}
                ]
            }
        },
        "XXXX5678":
            {
                "result": "00",
                "result_message": "检测通过或查询有记录",
                "content": {
                    "license_plate": "渝FC8***",
                    "start_time": "201401",
                    "end_time": "201412",
                    "over_speed_times": 2,
                    "over_speed_list": [{
                        "count_month": "201506",
                        "month_times": 2,
                        "section": "北京通州站-河北燕郊站，河北廊坊站-天津蓟县站",}
                    ]
                }
            },
    }
"""
import logging

from vendor.utils.defaults import *

logger = logging.getLogger('apps.common')


class Handle(object):
    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        输入:
        接口名称：'high_way_over_speed'  高速超速统计查询
        字段名称：'month_times'  超速次数 str

        计算逻辑: 先从车牌号(car_umber)特征根据车牌号查询每月每辆车的超速信息,
                 再汇总所有车的超速次数,输出类型为int

        输出:
        特征名称: 'overspeed_count' 超速次数 str
        """
        result = {'overspeed_count': UnsignedIntTypeDefault}

        try:
            month_times = 0
            for card, card_record in self.data.items():
                if card_record.get('result') == '00':
                    base_data = card_record.get("content", {}).get("over_speed_list", [])
                    for car_data in base_data:
                        if str(car_data.get("month_times", 0)).isdigit():
                            month_times += int(car_data.get("month_times", 0))

            result['overspeed_count'] = month_times

        except Exception as e:
            logging.error(e.message)

        return result
