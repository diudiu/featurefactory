# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2013- DIGCREDIT, All Rights Reserved.
    -----------------------------------------------------------
    Author: Z.L
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
                "over_load_times": 2,
                "over_load_list": [{
                    "count_month": "201506",
                    "month_times": 5,}
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
                    "over_load_times": 5,
                    "over_load_list": [{
                        "count_month": "201506",
                        "month_times": 1,}
                    ]
                }
            },
    }
"""
import logging

logger = logging.getLogger('apps.common')


class Handle(object):
    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        输入:
        接口名称：
        'high_way_over_load': 高速超载统计查询
        字段名称：'month_times': 超载总次数 str

        计算逻辑: 先从车牌号(car_umber)特征获取车牌号列表,再汇总所有车的超载次数

        输出:
        特征名称: 'overload_count': 超速次数 int
        """
        try:
            result = {'overload_count': 9999}
            month_times = 0
            # 查询所有车的超载次数进行汇总
            for card, card_record in self.data.items():
                if card_record.get('result') == '00':
                    base_data = card_record.get("content", {}).get("over_load_list", [])
                    for car_data in base_data:
                        if str(car_data.get("month_times", 0)).isdigit():
                            month_times += int(car_data["month_times"])
            result['overload_count'] = month_times

        except Exception as e:
            logging.error(e.message)
        finally:
            return result

