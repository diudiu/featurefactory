# -*- coding:utf-8 -*-
import unittest
from featurefactory.studio.lp_dataocean_handle.lp_tianwang_multi_loan import Handle
data = {
    "result": "00",
    "result_message": "检测通过或查询有记录",
    "content": [
        {
            "type": "黑名单",
            "date": "",
            "desc": "黑名单_网贷黑名单_网贷帮手",
            "originalRet": {
                "no": 0,
                "url": "",
                "abstract": "",
                "title": "",
                "class": "",
                "search_type": "",
                "search_word": "",
            }
        }
    ]
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