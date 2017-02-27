# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2017- DIGCREDIT, All Rights Reserved.
    ----------------------------------------------
    Author: Sun Fei
    Date:  2017/1/22
    Change Activity:
"""
from vendor.utils.defaults import PositiveSignedTypeDefault
import logging

logger = logging.getLogger('apps.common')


class Handle(object):
    def __init__(self, data):
        self.data = data

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
        mobile_stability_dic = {'mobile_stability': PositiveSignedTypeDefault}
        try:
            if self.data['result'] == 0:
                tags = self.data['data']['tags']
                tel_number = '6666666'
                tel_str = '%s__' % tel_number

                def get_tel_value(strs):
                    tmp = []
                    for i in ['M1', 'M2', 'M3', 'M4', 'M5']:
                        if i in tags[strs]:
                            callTimes = tags[strs].get(i, {}).get('callTimes', 0)
                            calledTimes = tags[strs].get(i, {}).get('calledTimes', 0)
                            if not str(callTimes).replace('.', '').isdigit():
                                callTimes = 0
                            if not str(calledTimes).replace('.', '').isdigit():
                                calledTimes = 0
                            tmp.append(callTimes + calledTimes)
                    return tmp

                # 假如存在'138xxxxxxxx__'的格式，以此为准取m1-m5
                if tel_str in tags:
                    m1_m5_max = get_tel_value(tel_str)

                # 其他情况，以前5月加和最大值取m1-m5
                else:
                    m1_m5_max = []
                    for strs in tags:
                        m1_m5 = get_tel_value(strs)
                        if sum(m1_m5) > sum(m1_m5_max):
                            m1_m5_max = m1_m5
                total_calltimes_ave = 0
                mobile_stability = 0
                if len(m1_m5_max) > 0:
                    total_calltimes_ave = sum(m1_m5_max) / len(m1_m5_max)

                if total_calltimes_ave > 0 and len(m1_m5_max) > 0:
                    mobile_stability = (sum([i ** 2 for i in m1_m5_max]) / len(m1_m5_max)) ** 0.5
                    mobile_stability = mobile_stability / total_calltimes_ave
                mobile_stability_dic['mobile_stability'] = round(mobile_stability, 4)

        except Exception as e:
            logging.error(e.message)

        return mobile_stability_dic


