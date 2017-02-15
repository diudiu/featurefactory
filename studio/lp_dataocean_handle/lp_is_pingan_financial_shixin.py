# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: LJY
    Date:  2017/01/18
    Change Activity:

    data ={
        'data':
            {
                'name':'姓名 ',
                'idCard':'身份证 ',
                'phone':'手机号',
                'imsi':'imsi',
                'imei':'imei',
                'areaCode':'地区编号',
                'others':[
                    {
                        'orgLostContact': '2015-09-11 09:49:52',#机构失联
                        'bankLostContact': '2015-08-23 11:23:50',#银行失联
                        'orgOverduePeriod': '',#机构逾期期数
                        'bankOverduePeriod': '',#银行逾期期数
                        'seriousOverdueTime': '2016-04-24 11:44:20',#最后一次严重逾期时间
                        'dunTelCallTime': '20160524',#最后一次催收电话的呼叫时间
                        'orgLitigation': '',#机构诉讼
                        'bankLitigation': '',#银行诉讼
                        'orgBlackList': [
                            {
                                'value':'abc',   #机构名称
                                'org_code':'123', #机构编号
                                'imsi':'135',  #匹配的加密imsi
                             }
                        ] ,#列为黑名单的机构
                        'orgOneMonthOvedue': '',   #开户30天有逾期
                        'matchType':'',    #匹配查询的类型(phone/imei/imsi)
                        'matchValue':'',    #匹配查询类型的值
                        'matchId':'' #匹配查询到的imsi的md5值
                    }
                ]
            }
    }
"""
import logging

logger = logging.getLogger('apps.common')


class Handle(object):

    def __init__(self, data):
        self.data = data

    def handle(self):
        """
        接口名称：猎聘金融
        字段名称：result_dict          返回结果

        输出:
        特征名称:  is_pingan_financial_shixin
        字段名称:
        'is_pingan_financial_shixin' 是否命中金融失信名单
        """
        try:
            result = {'is_pingan_financial_shixin': 9999}
            base_data = self.data["data"]['others']
            assert type(base_data) == list
            if len(base_data) > 0:
                result['is_pingan_financial_shixin'] = True
            else:
                result['is_pingan_financial_shixin'] = False

        except Exception as e:
            logging.error(e.message)
        finally:
            return result
