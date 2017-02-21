# -*- coding:utf-8 -*-
import unittest
from studio.lp_dataocean_handle.lp_is_skyeye_black import Handle
data = {
    "result": "00",
    "result_message": "检测通过或查询有记录",
    "content": [{
        "date": "0000-00-00",
        "originalRet": {
            "illegal_type": "",
            "id_card_name": "楚亮",
            "home_address": "湖南省湘潭市雨湖区人民路２４号",
            "user_type": "",
            "sex": 0,
            "source_email": None,
            "black_level": "1",
            "execute_status": "",
            "id": 15851,
            "borrow_amount": "4000.00",
            "court": "",
            "source_mobile": "13873275214",
            "case_detail": "",
            "company_name": "",
            "performed_part": "",
            "publish_source": "拍拍贷",
            "source_card": None,
            "qq": None,
            "publish_time": "0000-00-00",
            "id_card_code": "430321198402069014",
            "over_due_days": 0,
            "mobile_equipment_number": "",
            "crawl_time": "2015-06-09",
            "case_code": "",
            "arrears_limit": "0.00",
            "fixed_telephone": "0731-57894381",
            "over_due_nums": 0,
            "mobile": "13873275214",
            "email": "419650792@qq.com",
            "publish_date": "",
            "unperform_part": "",
            "company_address": "",
            "source_equipment_number": None,
        },
        "type": "拍拍贷",
        "desc": "楚亮"
    }],
}


results = [u'00', u'11', u'22', '']


class TestPlugin(unittest.TestCase):

    def setUp(self):
        self.data = data
        self.results = results

    def test_tianyan_black(self):
        data = self.data.copy()
        for result in results:
            data["result"] = result
            handler = Handle(data)
            res = handler.handle()
            print res


if __name__ == '__main__':
    unittest.main()