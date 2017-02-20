# -*- coding:utf-8 -*-

import unittest
import json
from studio.lp_dataocean_handle.lp_cur_employee_number import Handle

data = {
    "result": "00" ,
    "result_message" : "检测通过或查询有记录",
    "content": {
                "operation_start": "2009-09-08",
                "register_code": "371102200011819",
                "currency": "人民币",
                "postal_code": "",
                "national_economy_code": "5165",
                "enterprise_type": "有限责任公司(自然人投资或控股)",
                "operation_project": "矿产品(国家专控除外)、煤炭、钢材、木制品、建材、初级农产品、工程机械、机电设备、金属制品、摩托车、家用电器、文化用品、橡胶制品、化工产品（危险化学品及易制毒化学品除外）销售；普通货物进出口(法律禁止和国家专控除外限制的项目需取得许可证方可经营)。(依法须经批准的项目，经相关部门批准后方可开展经营活动)。",
                "industry_category_code": "F",
                "registered_assets": "1000.000000",
                "legal_person_name": "孙国庆",
                "authority_code": "",
                "start_business_date": "2009-09-08",
                "annual_inspection_year": "",
                "operation_scope_form": "矿产品(国家专控除外)、煤炭、钢材、木制品、建材、初级农产品、工程机械、机电设备、金属制品、摩托车、家用电器、文化用品、橡胶制品、化工产品（危险化学品及易制毒化学品除外）销售；普通货物进出口(法律禁止和国家专控除外限制的项目需取得许可证方可经营)。(依法须经批准的项目，经相关部门批准后方可开展经营活动)。",
                "staff_count": "",
                "revoke_date": "",
                "registration_authority": "日照市工商行政管理局东港分局",
                "tp_deal_identifying": "",
                "enterprise_phone": "",
                "annual_inspection_date": "",
                "authority_name": "",
                "organization_code": "",
                "address": "日照市黄海一路兴业国际商城001号楼01单元903号",
                "enterprise_name": "山东南港国际贸易有限公司",
                "operation_end": "2019-09-07",
                "organization_code_end": "",
                "organization_code_start": "",
                "licensing_project": "",
                "cancellation_date": "",
                "operation_status": "在营（开业）",
                "operation_scope": "矿产品(国家专控除外)、煤炭、钢材、木制品、建材、初级农产品、工程机械、机电设备、金属制品、摩托车、家用电器、文化用品、橡胶制品、化工产品（危险化学品及易制毒化学品除外）销售；普通货物进出口(法律禁止和国家专控除外限制的项目需取得许可证方可经营)。(依法须经批准的项目，经相关部门批准后方可开展经营活动)。"
            },
}

staff_counts = ["18", "20", "99", "10000000", "-1", "None"]


class TestPlugin(unittest.TestCase):

    def setUp(self):
        self.data = data

    def test_lp_cur_employee_number(self):
        data = self.data.copy()
        a = open('res.txt', 'w+')
        for staff_count in staff_counts:
            data['content']['staff_count'] = staff_count
            handler = Handle(data)
            res = handler.handle()
            a.write(json.dumps(res) + '\n')
        a.close()

if __name__ == '__main__':
    unittest.main()