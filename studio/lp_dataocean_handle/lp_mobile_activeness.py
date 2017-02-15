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
from vendor.errors.fecture_error import MyException
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
                  contactAmount       联系人个数

        输出：
        特征名称：mobile_activeness   申请人手机号活跃度
        """
        try:
            mobile_activeness_dic = {'mobile_activeness': 9999}  # 9999：异常
            tags = self.data['data']['tags']
            if not isinstance(tags, dict):
                raise MyException(message='get (tags) fail')
            tel_number = self.tel_number
            tel_str = str(tel_number) + '__'

            # 假如存在'138xxxxxxxx__'的格式，以此为准取m1-m5
            if tel_str in tags:
                m1 = tags[tel_str]['M1'].get('contactAmount', 0)
                m2 = tags[tel_str]['M2'].get('contactAmount', 0)
                m3 = tags[tel_str]['M3'].get('contactAmount', 0)
                m4 = tags[tel_str]['M4'].get('contactAmount', 0)
                m5 = tags[tel_str]['M5'].get('contactAmount', 0)
            # 其他情况，以前5月加和最大值取m1-m5
            else:
                tel_contactAmount_dic = {}
                for tel_str in tags:
                    tel_contactAmount_dic[tel_str] = tags[tel_str]['M1'].get('contactAmount', 0) + tags[tel_str]['M2'].get('contactAmount', 0) + tags[
                        tel_str]['M3'].get('contactAmount', 0) + tags[tel_str]['M4'].get('contactAmount', 0) + tags[tel_str]['M5'].get('contactAmount', 0)

                tel_str_final = max(
                    tel_contactAmount_dic.items(), key=lambda x: x[1])[0]
                m1 = tags[tel_str_final]['M1'].get('contactAmount', 0)
                m2 = tags[tel_str_final]['M2'].get('contactAmount', 0)
                m3 = tags[tel_str_final]['M3'].get('contactAmount', 0)
                m4 = tags[tel_str_final]['M4'].get('contactAmount', 0)
                m5 = tags[tel_str_final]['M5'].get('contactAmount', 0)

            mobile_activeness = (m1 + m2 + m3 + m4 + m5) / 5

            mobile_activeness_dic['mobile_activeness'] = round(mobile_activeness, 2)

        except MyException as e:
            logging.error(e.message)
        except Exception as e:
            logging.error(e.message)
        finally:
            return mobile_activeness_dic
