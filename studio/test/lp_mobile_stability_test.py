# -*- coding:utf-8 -*-

import unittest

from studio.lp_dataocean_handle.lp_mobile_stability import Handle

data = {
"trustutn_loan_phone":{
    "result": 0,
    "message": None,
    "res_data": {
        "tags": {
            "18920019795__": {
                "M0": {
                    "distributionOfContacts": {
                        "1": "16",
                        "2": "13",
                        "3": "1",
                        "4": "3",
                        "6": "2",
                        "7": "1",
                        "8": "1",
                        "10": "1",
                        "13": "2",
                        "22": "1",
                        "36": "1"
                    },
                    "dailyCallTimes": 8.901,
                    "hourStat": {
                        "night": 6,
                        "day": 158,
                        "morning": 14
                    },
                    "callTimes": '',
                    "calledTimes": 13,
                    "smsNotifications": None,
                    "activeShortest": 1,
                    "activeLongest": 79236,
                    "activeAverage": 9615.126,
                    "contactAmount": 42,
                    "month": "201701"
                },
                "M1": {
                    "distributionOfContacts": {
                        "3": "1",
                        "4": "1",
                        "5": "1"
                    },
                    "dailyCallTimes": 0.388,
                    "hourStat": {
                        "night": 0,
                        "day": 12,
                        "morning": 0
                    },
                    "callTimes": 6,
                    "calledTimes": '',
                    "smsNotifications": None,
                    "activeShortest": 2,
                    "activeLongest": 10888,
                    "activeAverage": 3377,
                    "contactAmount": 3,
                    "month": "201612"
                },
                "M6": {
                    "month": "201611"
                },
                "M3": {
                    "month": "201610"
                },
                "M4": {
                    "distributionOfContacts": {
                        "1": "4",
                        "2": "3"
                    },
                    "dailyCallTimes": 0.334,
                    "hourStat": {
                        "night": 0,
                        "day": 10,
                        "morning": 0
                    },
                    "callTimes": 8,
                    "calledTimes": 2,
                    "smsNotifications": None,
                    "activeShortest": 6,
                    "activeLongest": 59391,
                    "activeAverage": 9786.223,
                    "contactAmount": 7,
                    "month": "201609"
                },
                "M5": {
                    "distributionOfContacts": {
                        "1": "18",
                        "2": "11",
                        "3": "2",
                        "5": "1",
                        "6": "1",
                        "10": "1"
                    },
                    "dailyCallTimes": 2.162,
                    "hourStat": {
                        "night": 6,
                        "day": 55,
                        "morning": 6
                    },
                    "callTimes": 38,
                    "calledTimes": 9,
                    "smsNotifications": None,
                    "activeShortest": 2,
                    "activeLongest": 156909,
                    "activeAverage": 10155.107,
                    "contactAmount": 34,
                    "month": "201608"
                },
                "T6": {
                    "distributionOfContacts": {
                        "1": "17",
                        "2": "14",
                        "3": "3",
                        "5": "1",
                        "7": "1",
                        "11": "1"
                    },
                    "dailyCallTimes": 0.446,
                    "hourStat": {
                        "night": 6,
                        "day": 65,
                        "morning": 6
                    },
                    "callTimes": 46,
                    "calledTimes": 31,
                    "smsNotifications": None,
                    "activeShortest": 2,
                    "activeLongest": 156909,
                    "activeAverage": 10876.54,
                    "contactAmount": 37,
                    "month": "halfyear"
                }
            },
            "18920019796__": {
                "M0": {
                    "distributionOfContacts": {
                        "1": "16",
                        "2": "13",
                        "3": "1",
                        "4": "3",
                        "6": "2",
                        "7": "1",
                        "8": "1",
                        "10": "1",
                        "13": "2",
                        "22": "1",
                        "36": "1"
                    },
                    "dailyCallTimes": 8.901,
                    "hourStat": {
                        "night": 6,
                        "day": 158,
                        "morning": 14
                    },
                    "callTimes": '',
                    "calledTimes": 103,
                    "smsNotifications": None,
                    "activeShortest": 1,
                    "activeLongest": 79236,
                    "activeAverage": 9615.126,
                    "contactAmount": 42,
                    "month": "201701"
                },
                "M1": {
                    "distributionOfContacts": {
                        "3": "1",
                        "4": "1",
                        "5": "1"
                    },
                    "dailyCallTimes": 0.388,
                    "hourStat": {
                        "night": 0,
                        "day": 12,
                        "morning": 0
                    },
                    "callTimes": '',
                    "calledTimes": 6,
                    "smsNotifications": None,
                    "activeShortest": 2,
                    "activeLongest": 10888,
                    "activeAverage": 3377,
                    "contactAmount": 3,
                    "month": "201612"
                },
                "M2": {
                    "month": "201611"
                },
                "M3": {
                    "month": "201610"
                },
                "M4": {
                    "distributionOfContacts": {
                        "1": "4",
                        "2": "3"
                    },
                    "dailyCallTimes": 0.334,
                    "hourStat": {
                        "night": 0,
                        "day": 10,
                        "morning": 0
                    },
                    "callTimes": 8,
                    "calledTimes": '',
                    "smsNotifications": None,
                    "activeShortest": 6,
                    "activeLongest": 59391,
                    "activeAverage": 9786.223,
                    "contactAmount": 7,
                    "month": "201609"
                },
                "M5": {
                    "distributionOfContacts": {
                        "1": "18",
                        "2": "11",
                        "3": "2",
                        "5": "1",
                        "6": "1",
                        "10": "1"
                    },
                    "dailyCallTimes": 2.162,
                    "hourStat": {
                        "night": 6,
                        "day": 55,
                        "morning": 6
                    },
                    "callTimes": 38,
                    "calledTimes": 9,
                    "smsNotifications": None,
                    "activeShortest": 2,
                    "activeLongest": 156909,
                    "activeAverage": 10155.107,
                    "contactAmount": 34,
                    "month": "201608"
                },
                "T6": {
                    "distributionOfContacts": {
                        "1": "17",
                        "2": "14",
                        "3": "3",
                        "5": "1",
                        "7": "1",
                        "11": "1"
                    },
                    "dailyCallTimes": 0.446,
                    "hourStat": {
                        "night": 6,
                        "day": 65,
                        "morning": 6
                    },
                    "callTimes": 46,
                    "calledTimes": 31,
                    "smsNotifications": None,
                    "activeShortest": 2,
                    "activeLongest": 156909,
                    "activeAverage": 10876.54,
                    "contactAmount": 37,
                    "month": "halfyear"
                }
            },
            "18920019796_8a404758b8f8b87c70006b8e9f4614db_": {
                "M0": {
                    "distributionOfContacts": {
                        "1": "16",
                        "2": "13",
                        "3": "1",
                        "4": "3",
                        "6": "2",
                        "7": "1",
                        "8": "1",
                        "10": "1",
                        "13": "2",
                        "22": "1",
                        "36": "1"
                    },
                    "dailyCallTimes": 8.901,
                    "hourStat": {
                        "night": 6,
                        "day": 158,
                        "morning": 14
                    },
                    "callTimes": 75,
                    "calledTimes": 13,
                    "smsNotifications": None,
                    "activeShortest": 1,
                    "activeLongest": 79236,
                    "activeAverage": 9615.126,
                    "contactAmount": 42,
                    "month": "201701"
                },
                "M1": {
                    "distributionOfContacts": {
                        "3": "1",
                        "4": "1",
                        "5": "1"
                    },
                    "dailyCallTimes": 0.388,
                    "hourStat": {
                        "night": 0,
                        "day": 12,
                        "morning": 0
                    },
                    "callTimes": 6,
                    "calledTimes": None,
                    "smsNotifications": None,
                    "activeShortest": 2,
                    "activeLongest": 10888,
                    "activeAverage": 3377,
                    "contactAmount": 3,
                    "month": "201612"
                },
                "M2": {
                    "month": "201611"
                },
                "M3": {
                    "month": "201610"
                },
                "M4": {
                    "distributionOfContacts": {
                        "1": "4",
                        "2": "3"
                    },
                    "dailyCallTimes": 0.334,
                    "hourStat": {
                        "night": 0,
                        "day": 10,
                        "morning": 0
                    },
                    "callTimes": 8,
                    "calledTimes": 20,
                    "smsNotifications": None,
                    "activeShortest": 6,
                    "activeLongest": 59391,
                    "activeAverage": 9786.223,
                    "contactAmount": 7,
                    "month": "201609"
                },
                "M5": {
                    "distributionOfContacts": {
                        "1": "18",
                        "2": "11",
                        "3": "2",
                        "5": "1",
                        "6": "1",
                        "10": "1"
                    },
                    "dailyCallTimes": 2.162,
                    "hourStat": {
                        "night": 6,
                        "day": 55,
                        "morning": 6
                    },
                    "callTimes": 3,
                    "calledTimes": 2,
                    "smsNotifications": None,
                    "activeShortest": 2,
                    "activeLongest": 156909,
                    "activeAverage": 10155.107,
                    "contactAmount": 34,
                    "month": "201608"
                },
                "T6": {
                    "distributionOfContacts": {
                        "1": "17",
                        "2": "14",
                        "3": "3",
                        "5": "1",
                        "7": "1",
                        "11": "1"
                    },
                    "dailyCallTimes": 0.446,
                    "hourStat": {
                        "night": 6,
                        "day": 65,
                        "morning": 6
                    },
                    "callTimes": 46,
                    "calledTimes": 31,
                    "smsNotifications": None,
                    "activeShortest": 2,
                    "activeLongest": 156909,
                    "activeAverage": 10876.54,
                    "contactAmount": 37,
                    "month": "halfyear"
                }
            }
        }
    },
    "apply_base": {
        "latitude": 145.23342,
        "name": "章撒",
        "mobile": "18989821092",
        "callback": "http://127.0.0.1/syph-re/api/credit/result/",
        "application_on": "2017-02-01 12:20:10",
        "contacts": 30,
        "card_id": "41140219890313739X",
        "longitudu": 23.45678
    }
}}


class TestPlugin(unittest.TestCase):

    def setUp(self):
        self.data = data

    def test_test(self):
        data = self.data
        for i in data['apply_data']:
            h = Handle(data, i)
            res = h.handle()
            print res

if __name__ == '__main__':
    unittest.main()

