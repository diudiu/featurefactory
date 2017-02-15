import unittest
from featurefactory.studio.lp_dataocean_handle.lp_telecom_mobile_identity_s import Handle

data = {
        "result": "00",
        "result_message": "",
        "content": {}
    }

results = [u'00', u'11', u'22', '', None]

class TestPlugin(unittest.TestCase):

    def setUp(self):
        self.data = data
        self.results = results

    def test_unicom_mobile_identity_s(self):
        data = self.data.copy()
        for result in results:
            data["result"] = result
            handler = Handle(data)
            res = handler.handle()
            print res


if __name__ == '__main__':
    unittest.main()