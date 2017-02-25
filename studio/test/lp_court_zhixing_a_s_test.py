# -*- coding:utf-8 -*-

import unittest

from studio.lp_dataocean_handle.lp_is_court_zhixing import Handle

data = {
    "result": "00",
    "result_message": "检测通过或查询有记录",
    "content":
        {
            "zhixing_list":
                [
                    {
                        "case_create_time": "2016-03-01",
                        "entity_id": "433031196210056032",
                        "court": "通道侗族自治县人民法院",
                        "entity_name": "吴永荣",
                        "case_code": "(2016)湘1230执00016号",
                        "case_state": "执行中",
                        "exec_money": "237000"
                    },
                    {
                        "case_create_time": "2015-09-25",
                        "entity_id": "433031196210056032",
                        "court": "中山市第一人民法院",
                        "entity_name": "吴永荣",
                        "case_code": "(2015)中-法执字第08491号",
                        "case_state": "执行中",
                        "exec_money": "21651.16"
                    },
                    {
                        "case_create_time": "2015-09-21",
                        "entity_id": "433031196210056032",
                        "court": "中山市第一人民法院",
                        "entity_name": "吴永荣",
                        "case_code": "(2015)中-法执字第08293号",
                        "case_state": "执行中",
                        "exec_money": "50392.22"
                    },
                    {
                        "case_create_time": "2015-09-21",
                        "entity_id": "433031196210056032",
                        "court": "中山市第一人民法院",
                        "entity_name": "吴永荣",
                        "case_code": "(2015)中一法执字第08293号",
                        "case_state": "执行中",
                        "exec_money": "50392.22"
                    },
                    {
                        "case_create_time": "2015-01-09",
                        "entity_id": "433031196210056032",
                        "court": "中山市第二人民法院",
                        "entity_name": "吴永荣",
                        "case_code": "(2015)中二法执字第00706号",
                        "case_state": "执行中",
                        "exec_money": "305800"
                    }
                ]
        }
}
test = [u'00', u'11', u'22']
result = [1, 0, 0]


class TestPlugin(unittest.TestCase):
    def setUp(self):
        self.data = data

    def test_test(self):
        data = self.data.copy()
        for t, r in zip(test, result):
            data["result"] = t
            handler = Handle(data)
            res = handler.handle()
            assert res.values()[0] == r

if __name__ == '__main__':
    unittest.main()
