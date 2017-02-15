# -*- coding:utf-8 -*-
import unittest
from studio.lp_dataocean_handle.lp_airfare_sum_12 import Handle

data = {
          "result": "00",
          "result_message": "检测通过或查询有记录",
          "content": {
                "id_card_name": "吴*",
                "id_card_code": "513722198908***43X",
                "flight_times": 2,
                "flight_month": "201502",
                "flight_max": 2,
                "average_discount": 100,
                "business_class_count": 0,
                "executive_class_count": 0,
                "tourist_class_count": 2,
                "from_city": "广元1次,北京1次,",
                "destination_city ": "北京1次,广元1次,",
                "inland_count": 2,
                "international_count": 0,
                "free_count": 0,
                "average_price": 1340.00,
                "delay_time": 40,
                "average_delay_time": 20,
                "average_ticket_day": 68,
                "last_date": "20150228",
                "last_from_city": "广元",
                "last_destination_city": "北京",
                "total_distance": 2810,
          },
}
results = ['00', '11', '22', '']


class TestPlugin(unittest.TestCase):

    def setUp(self):
        self.data = data
        self.results = results

    def test_airfare_sum_12(self):
        data = self.data.copy()
        for result in results:
            data["result"] = result
            handler = Handle(data)
            res = handler.handle()
            print res


if __name__ == '__main__':
    unittest.main()