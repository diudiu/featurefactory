# -*- coding:utf-8 -*-

import unittest

from studio.lp_dataocean_handle.lp_marital_status import Handle

data = {
    "result": "00",
    "result_message": "检测通过或查询有记录",
    'content': {
        'id_card_name': '李..',
        'marital_status': '10',
        'id_card_code': '1306251....',
        'verify': '一致',
        'company': '暂无',
        'nation': '汉族',
        'former_name': '',
        'native_place': '河北省保定市徐水县',
        'birthday': '1988-09-10',
        'birth_place': '河北省保定市徐水县',
        'sex_id': '2',
        'photo': '',
        'education': '大学本科（简称"大学"）',
        'address': '河北省保定市徐水区高林村镇'
    }
}
marital_status = "10"


class TestPlugin(unittest.TestCase):
    def setUp(self):
        self.data = data

    def test_lp_marital_status(self):

        data = self.data
        h = Handle(data)
        res = h.handle()
        self.assertEqual(res['marital_status'], data['content']['marital_status'])

        data['result'] = '11'
        h = Handle(data)
        res = h.handle()
        self.assertEqual(res['marital_status'], 9999)

        data['content']['marital_status'] = None

        handler = Handle(data)
        res = handler.handle()
        self.assertEqual(res['marital_status'], 9999)

if __name__ == '__main__':
    unittest.main()
