# -*- coding:utf-8 -*-

import unittest

from  featurefactory.studio.lp_dataocean_handle.lp_unicom_income_expense_comparison import Handle

data = {
    "result": "00",
    "result_message": "检测通过或查询有记录",
    "content": {
        "bank_count": 1,
        "credit_card_count": 2,
        "debit_card_count": 3,
        "last12": {
            "credit": {
                "charge_off_range": "b",
                "charge_off_times": 25,
                "income_times": 35,
                "income_range": "c"
            },
            "debit": {
                "charge_off_range": "13",
                "charge_off_times": 138,
                "income_times": 16,
                "income_range": "20"
            }
        }
    }
}
income_range = "10"
charge_off_ranges = ['0', '1', '2', '8', '25']
results = ['00', '11', '22', None]


class TestPlugin(unittest.TestCase):

    def setUp(self):
        self.data = data

    def test_lp_unicom_income_expense_comparison(self):
        data = self.data.copy()
        for result in results:
            data["result"] = result
            if data["result"] != '00':
                handler = Handle(data)
                res = handler.handle()
                print res
            elif data["result"] == '00':
                data['content']['last12']['debit']['income_range'] = income_range
                data['content']['last12']['debit']['income_range'] = income_range
                for charge_off_range in charge_off_ranges:
                    data['content']['last12']['debit']['charge_off_range'] = charge_off_range
                    handler = Handle(data)
                    res = handler.handle()
                    print res


if __name__ == '__main__':
    unittest.main()
