# -*- coding:utf-8 -*-

import unittest
<<<<<<< HEAD
from studio.lp_dataocean_handle.lp_court_shixin_a_s import Handle

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
results = [u'00', u'11', u'22', '']


class TestPlugin(unittest.TestCase):
=======
from studio.lp_dataocean_handle.lp_court_zhixing_a_s import  Handle
data = {
    "result_message": "检测通过或查询有记录",
        "result": "00",
        "content": {}

    }
results = [u'00', u'11', u'22', '']

class TestPlugin(unittest.TestCase):

>>>>>>> ed2dd7ad4669a84c046eb83ac35f79ee9fc1c10c
    def setUp(self):
        self.data = data
        self.results = results

    def test_court_shixin_a_s(self):
        data = self.data.copy()
        for result in results:
            data["result"] = result
<<<<<<< HEAD
            if data["result"] != '00':
                handler = Handle(data)
                res = handler.handle()
                print res
            elif data["result"] == '00':
                handler = Handle(data)
                res = handler.handle()
                print res


if __name__ == '__main__':
    unittest.main()
=======
            handler = Handle(data)
            res = handler.handle()
            print res

if __name__ == '__main__':
    unittest.main()
>>>>>>> ed2dd7ad4669a84c046eb83ac35f79ee9fc1c10c
