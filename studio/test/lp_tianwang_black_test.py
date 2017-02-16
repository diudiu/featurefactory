# -*- coding:utf-8 -*-
import unittest
from studio.lp_dataocean_handle.lp_tianwang_black import Handle
data = {
    "result": "00",
    "result_message": "检测通过或查询有记录",
    "content": [
        {
            "type": "商品交易",
            "date": "",
            "desc": "<a href=\"http://bagideal.com/goods_44652152990.html\" style=\"color:#E3AD1C\"  target=\"_blank\">WOOG韩版男装2014秋季新款蓝色小脚休闲裤男士纯色潮流修身型...</a>",
            "originalRet": {
                "no": 8,
                "url": "http://bagideal.com/goods_44652152990.html",
                "abstract": "1398**0 品牌: 价格: 369.00 参数: 卖点: 标签: 纯色,小脚,长裤,修身,男装 WOOG韩版男装2014秋季新款蓝色小脚休闲裤男士纯色潮流修身型长裤评价 我要点评:  [热门评论] 榆林榆阳区买家15614...",
                "title": "WOOG韩版男装2014秋季新款蓝色小脚休闲裤男士纯色潮流修身型...",
                "search_type": "phone",
                "search_word": "13**000",
                "class": "商品交易",
            }
        },
    ]
}

results = [u'00', u'11', u'22', '']


class TestPlugin(unittest.TestCase):

    def setUp(self):
        self.data = data
        self.results = results

    def test_tianwang_black(self):
        data = self.data.copy()
        for result in results:
            data["result"] = result
            handler = Handle(data)
            res = handler.handle()
            print res


if __name__ == '__main__':
    unittest.main()