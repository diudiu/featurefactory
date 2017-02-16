# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2017- DIGCREDIT, All Rights Reserved.
    ----------------------------------------------
    Author: Sun Fei
    Date:  2017/1/22
    Change Activity:
"""
import logging

logger = logging.getLogger('apps.common')


class Handle(object):

    def __init__(self, data, tel_number):
        self.data = data
        self.tel_number = tel_number

    def handle(self):
        """
        接口名称：凭安反欺诈服务接口
        字段名称：tel_number          申请人手机号
                  tags                电话标记
                  callTimes           主叫次数
                  calledTimes         被叫次数

        输出：
        特征名称：mobile_stability    申请人手机号稳定度
        """

        mobile_stability_dic = {'mobile_stability': 9999.0}  # 9999：异常

        try:
            tags = self.data['data']['tags']
        except Exception:
            # TODO log this error
            return mobile_stability_dic

        if not isinstance(tags, dict):
            return mobile_stability_dic

        tel_number = self.tel_number
        tel_str = str(tel_number) + '__'

        # 假如存在'138xxxxxxxx__'的格式，以此为准取m1-m5
        if tel_str in tags:
            m1 = tags[tel_str]['M1'].get(
                'callTimes', 0) + tags[tel_str]['M1'].get('calledTimes', 0)
            m2 = tags[tel_str]['M2'].get(
                'callTimes', 0) + tags[tel_str]['M2'].get('calledTimes', 0)
            m3 = tags[tel_str]['M3'].get(
                'callTimes', 0) + tags[tel_str]['M3'].get('calledTimes', 0)
            m4 = tags[tel_str]['M4'].get(
                'callTimes', 0) + tags[tel_str]['M4'].get('calledTimes', 0)
            m5 = tags[tel_str]['M5'].get(
                'callTimes', 0) + tags[tel_str]['M5'].get('calledTimes', 0)
        # 其他情况，以前5月加和最大值取m1-m5
        else:
            tel_total_calltimes_dic = {}
            for tel_str in tags:
                tel_total_calltimes_dic[tel_str] = tags[tel_str]['M1'].get(
                    'callTimes', 0) + tags[tel_str]['M1'].get('calledTimes', 0)
                + tags[tel_str]['M2'].get(
                    'callTimes', 0) + tags[tel_str]['M2'].get('calledTimes', 0)
                + tags[tel_str]['M3'].get(
                    'callTimes', 0) + tags[tel_str]['M3'].get('calledTimes', 0)
                + tags[tel_str]['M4'].get(
                    'callTimes', 0) + tags[tel_str]['M4'].get('calledTimes', 0)
                + tags[tel_str]['M5'].get(
                    'callTimes', 0) + tags[tel_str]['M5'].get('calledTimes', 0)
            tel_str_final = max(
                tel_total_calltimes_dic.items(), key=lambda x: x[1])[0]
            m1 = tags[tel_str_final]['M1'].get(
                'callTimes', 0) + tags[tel_str_final]['M1'].get('calledTimes', 0)
            m2 = tags[tel_str_final]['M2'].get(
                'callTimes', 0) + tags[tel_str_final]['M2'].get('calledTimes', 0)
            m3 = tags[tel_str_final]['M3'].get(
                'callTimes', 0) + tags[tel_str_final]['M3'].get('calledTimes', 0)
            m4 = tags[tel_str_final]['M4'].get(
                'callTimes', 0) + tags[tel_str_final]['M4'].get('calledTimes', 0)
            m5 = tags[tel_str_final]['M5'].get(
                'callTimes', 0) + tags[tel_str_final]['M5'].get('calledTimes', 0)

        total_calltimes_ave = (m1 + m2 + m3 + m4 + m5) / 5
        mobile_stability = ((m1 ** 2 + m2 ** 2 + m3 ** 2 +
                             m4 ** 2 + m5 ** 2) / 5) ** 0.5 / total_calltimes_ave
        mobile_stability_dic['mobile_stability'] = round(
            mobile_stability, 4)

        return mobile_stability_dic
