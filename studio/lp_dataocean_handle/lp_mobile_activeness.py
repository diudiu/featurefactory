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

    def __init__(self, data,tel_number):
        self.data = data
        self.tel_number = tel_number


    def handle(self):
        """
        接口名称:凭安反欺诈服务接口
        字段名称:tel_number          申请人手机号
                  tags                电话标记
                  contactAmount       联系人个数

        输出:
        特征名称:mobile_activeness   申请人手机号活跃度
        """
        mobile_activeness_dic = {'mobile_activeness': PositiveSignedTypeDefault}
        try:
            if self.data['result'] == 0:
                tags = self.data['data']['tags']
                tags_key = tags.keys()
                if not isinstance(tags, dict):
                    return mobile_activeness_dic
                tel_num = self.tel_number['mobile']
                tel_str = '%s__' % tel_num
                # 假如存在'138xxxxxxxx__'的格式，以此为准取m1-m5

                def get_m_value(tel_str_m):
                    m_contact_amount_list = []
                    m_list = ['M1', 'M2', 'M3', 'M4', 'M5']
                    for i in m_list:
                        if i in tags[tel_str_m]:
                            m_contact_amount = tags[tel_str_m].get(i, {}).get('contactAmount', 0)
                            if not str(m_contact_amount).replace('.', '').isdigit():
                                m_contact_amount = 0
                            m_contact_amount_list.append(m_contact_amount)
                    return m_contact_amount_list
                if tel_str in tags:
                    m_amount = get_m_value(tel_str)
                    m_arv = sum(m_amount)/len(m_amount)
                    mobile_activeness_dic['mobile_activeness'] = round(m_arv, 2)
                else:
                    m1_m5_list = []
                    for strs in tags_key:
                        m1_m5 = get_m_value(strs)
                        m1_m5_list.append(sum(m1_m5))
                    m1_m5_max = max(m1_m5_list)
                    tel_tag_result = m1_m5_list.index(m1_m5_max)
                    tel_tag_result = tags_key[tel_tag_result]
                    m_avr = m1_m5_max/len(get_m_value(tel_tag_result))
                    mobile_activeness_dic['mobile_activeness'] = round(m_avr, 2)
        except Exception as e:
            logging.error(e.message)
        return mobile_activeness_dic
