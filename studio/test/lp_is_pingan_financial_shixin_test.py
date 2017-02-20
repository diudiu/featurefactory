# -*- coding:utf-8 -*-

import unittest

from studio.lp_dataocean_handle.lp_is_pingan_financial_shixin import Handle

data = {
    'data':
        {
            'name': '姓名 ',
            'idCard': '身份证 ',
            'phone': '手机号',
            'imsi': 'imsi',
            'imei': 'imei',
            'areaCode': '地区编号',
            'others': [
                {
                    'orgLostContact': '2015-09-11 09:49:52',  # 机构失联
                    'bankLostContact': '2015-08-23 11:23:50',  # 银行失联
                    'orgOverduePeriod': '',  # 机构逾期期数
                    'bankOverduePeriod': '',  # 银行逾期期数
                    'seriousOverdueTime': '2016-04-24 11:44:20',  # 最后一次严重逾期时间
                    'dunTelCallTime': '20160524',  # 最后一次催收电话的呼叫时间
                    'orgLitigation': '',  # 机构诉讼
                    'bankLitigation': '',  # 银行诉讼
                    'orgBlackList': [
                        {
                            'value': 'abc',  # 机构名称
                            'org_code': '123',  # 机构编号
                            'imsi': '135',  # 匹配的加密imsi
                        }
                    ],  # 列为黑名单的机构
                    'orgOneMonthOvedue': '',  # 开户30天有逾期
                    'matchType': '',  # 匹配查询的类型(phone/imei/imsi)
                    'matchValue': '',  # 匹配查询类型的值
                    'matchId': ''  # 匹配查询到的imsi的md5值
                }
            ]
        }
}


class TestPlugin(unittest.TestCase):
    def setUp(self):
        self.data = data

    def test_lp_is_pingan_financial_shixin(self):
        handler = Handle(self.data)
        res = handler.handle()
        self.assertEqual(res['is_pingan_financial_shixin'], 1)

        self.data['data']['others'] = []
        handler = Handle(self.data)
        res = handler.handle()
        self.assertEqual(res['is_pingan_financial_shixin'], 0)


if __name__ == '__main__':
    unittest.main()
