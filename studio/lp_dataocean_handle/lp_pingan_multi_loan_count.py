# -*- coding:utf-8 -*-
"""
    License DIGCREDIT-L.
    Copyright (c) 2013- DIGCREDIT, All Rights Reserved.
    -----------------------------------------------------------
    Author: Z.L
    Date:  2017/01/20
    Change Activity:
"""
import logging

logger = logging.getLogger('apps.common')


class Handle(object):
    def __init__(self, data):
        self.data = data

    def handle(self):

        """
        输入:
        接口名称：贷款信息
        字段名称：'org_names': 涉及机构数 int

        计算逻辑: 计算银行机构及非银机构发生贷款的公司数量总和

        输出:
        特征名称: 'pingan_multi_loan_count': 多头借贷公司数量 int
        """
        try:
            result = {
                'pingan_multi_loan_count': 9999,
            }
            if self.data.get('result', 0) == 0:
                org_count = 0
                records = self.data["data"]["record"]
                for record in records:
                    base_data = record.get("classification", [])  # 提取贷款信息列表
                    for data in base_data:
                        for in_data in data:
                            try:
                                other_org = int(data[in_data]["other"]["orgNums"])  # 提取其他机构贷款公司数量
                            except:
                                other_org = 0
                            try:
                                bank_org = int(data[in_data]["bank"]["orgNums"])  # 提取银行机构贷款公司数量
                            except:
                                bank_org = 0
                            org_count = org_count + other_org + bank_org

                result['pingan_multi_loan_count'] = org_count

        except Exception as e:
            logging.info(e.message)
        finally:
            return result




