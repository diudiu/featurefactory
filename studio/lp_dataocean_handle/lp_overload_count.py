# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2013- DIGCREDIT, All Rights Reserved.
    -----------------------------------------------------------
    Author: Z.L
    Date:  2017/02/17
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
from vendor.utils.defaults import UnsignedIntTypeDefault
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

        计算逻辑: 先从车牌号(car_umber)特征获取车牌号列表,根据车牌号查询每月每辆车的超载信息,
                 再汇总所有车的超载次数,输出类型为int

        输出:
        特征名称: 'overload_count': 超速次数 int
        """
        result = {'overload_count': UnsignedIntTypeDefault}

        try:
            month_times = 0
            for card, card_record in self.data.items():
                if card_record.get('result') == '00':  # result为'00'说明查询成功
                    base_data = card_record.get("content", {}).get("over_load_list", [])  # 提取车辆超载信息,提取失败返回空值
                    for car_data in base_data:  # 查询每辆车的超载次数进行汇总
                        if str(car_data.get("month_times", 0)).isdigit():
                            month_times += int(car_data["month_times"])
            result['overload_count'] = month_times

        except Exception as e:
            logging.error(e.message)
        finally:
            return result

