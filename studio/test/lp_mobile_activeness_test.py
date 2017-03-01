# -*- coding:utf-8 -*-
import unittest
from studio.lp_dataocean_handle.lp_mobile_activeness import Handle

data = {
    "trustutn_loan_phone": {
        "result": 0,
        "message": "",
        "res_data": {
            "commonContacts":
            {
                        "18920019795 | 17720038301": {
                            "M0": {
                                "count": "1",
                                "month": "201701"
                            },
                            "M1": {
                                "count": "1",
                                "month": "201612"} ,
                            "M2": {
                                "count": "0",
                                "month": "201611"
                            },
                            "M3": {
                                "count": "0",
                                "month": "201610"
                            },
                            "M4": {
                                "count": "1",
                                "month": "201609"
                            },
                            "M5": {
                                "count": "0",
                                "month": "201608"},
                            "T6": {
                                "97bf35e9449cbea50088c17f97af6049": {
                                    "18920019795": {
                                        "hourStat": {
                                            "night": 0,
                                            "day": 4,
                                            "morning": 0
                                        },
                                        "dailyCallTimes": 0.024,
                                        "rateOfCallPerAve": 0.0,
                                        "callTimes": 0,
                                        "calledTimes": 4,
                                        "earliestTime": 1483142287000,
                                        "latestTime": 1483142354000,
                                        "periodicity": False
                                    },
                                    "17720038301": {
                                        "hourStat": {"night": 0,
                                                     "day": 28,
                                                     "morning": 9
                                                     },
                                        "dailyCallTimes":0.214,
                                        "rateOfCallPerAve":0.0,
                                        "callTimes":18,
                                        "calledTimes":19,
                                        "earliestTime":1472722765000,
                                        "latestTime":1484717040000,
                                        "periodicity":False
                                    }
                                }
                            }
                        }
                    },
            "directCall":
            {
               "17720038301__":{
                   "M0":{
                       "hourStat":{
                           "night":0,
                           "day":25,
                           "morning":8
                       },
                       "dailyCallTimes":1.65,
                       "rateOfCallPerAve":0.0,
                       "callTimes":17,
                       "calledTimes":16,
                       "earliestTime":1483295919000,
                       "latestTime":1484717040000,
                       "month":"201701",
                       "periodicity":False
                   },
                   "M1":{
                       "hourStat":{
                           "night":0,
                           "day":0,
                           "morning":0
                       },
                       "dailyCallTimes":0.0,
                       "rateOfCallPerAve":0.0,
                       "callTimes":0,
                       "calledTimes":0,
                       "earliestTime":1484895878756,
                       "latestTime":1484895878756,
                       "month":"201612",
                       "periodicity":False
                   },
                   "M2":{
                       "hourStat":{
                           "night":0,
                           "day":0,
                           "morning":0
                       },
                       "dailyCallTimes":0.0,
                       "rateOfCallPerAve":0.0,
                       "callTimes":0,
                       "calledTimes":0,
                       "earliestTime":1484895878756,
                       "latestTime":1484895878756,
                       "month":"201611",
                       "periodicity":False},
                   "M3":{
                       "hourStat":{
                           "night":0,
                           "day":0,
                           "morning":0
                       },
                       "dailyCallTimes":0.0,
                       "rateOfCallPerAve":0.0,
                       "callTimes":0,
                       "calledTimes":0,
                       "earliestTime":1484895878756,
                       "latestTime":1484895878756,
                       "month":"201610",
                       "periodicity":False},
                   "M4":{
                       "hourStat":{
                           "night":0,
                           "day":1,
                           "morning":0
                       },
                       "dailyCallTimes":0.034,
                       "rateOfCallPerAve":0.0,
                       "callTimes":1,
                       "calledTimes":0,
                       "earliestTime":1472722765000,
                       "latestTime":1472722765000,
                       "month":"201609",
                       "periodicity":False},
                   "M5":{
                       "hourStat":{
                           "night":0,
                           "day":0,
                           "morning":0
                       },
                       "dailyCallTimes":0.0,
                       "rateOfCallPerAve":0.0,
                       "callTimes":0,
                       "calledTimes":0,
                       "earliestTime":1484895878756,
                       "latestTime":1484895878756,
                       "month":"201608",
                       "periodicity":False},
                   "T6":{
                       "hourStat":{
                           "night":0,
                           "day":26,
                           "morning":8
                       },
                       "dailyCallTimes":0.197,
                       "rateOfCallPerAve":0.0,
                       "callTimes":18,
                       "calledTimes":16,
                       "earliestTime":1472722765000,
                       "latestTime":1484717040000,
                       "periodicity":False
                   }
               }
           },
            "grayscale":
            {
               "18920019795__819020148A8F03B7CE75B530FCBD08E3":{
                   "M0":{
                       "NBFI":{
                           "contactTimes":1,
                           "orgNumbs":1,
                           "earliestTime":"20170108",
                           "latestTime":"20170108"
                       },
                       "bank":'',
                       "collectionAgency":'',
                       "month":"201701"
                   },
                   "M1":{
                       "month":"201612"
                   },
                   "M2":{
                       "month":"201611"
                   },
                   "M3":{
                       "month":"201610"
                   },
                   "M4":{
                       "month":"201609"
                   },
                   "M5":{
                       "NBFI":{
                           "contactTimes":1,
                           "orgNumbs":1,
                           "earliestTime":"20160824",
                           "latestTime":"20160824"
                       },
                       "bank":'',
                       "collectionAgency":'',
                       "month":"201608"
                   }
               }
           },
            "interactCommons":
            {
            },
            "tags":
            {"18989821092__5975452a1caf27d58030b62de41a92a0":
            {
                             "M0":
                              {"distributionOfContacts":{
                                  "3":"1",
                                  "2":"13",
                                  "1":"16",
                                  "10":"1",
                                  "7":"1",
                                  "6":"2",
                                  "4":"3",
                                  "22":"1",
                                  "36":"1",
                                  "8":"1",
                                  "13":"2"
                              },
                                  "dailyCallTimes":8.901,
                                  "hourStat":{
                                      "night":6,
                                      "day":158,
                                      "morning":14
                                  },
                                  "callTimes":75.0,
                                  "calledTimes":103.0,
                                  "smsNotifications":'',
                                  "activeShortest":1.0,
                                  "activeLongest":79236.0,
                                  "activeAverage":9615.126,

                                  "month":"201701"
                              },
                             "M1":{
                                 "distributionOfContacts":{
                                     "3":"1",
                                     "5":"1",
                                     "4":"1"
                                 },
                                 "dailyCallTimes":0.388,
                                 "hourStat":{
                                     "night":0,
                                     "day":12,
                                     "morning":0
                                 },
                                 "callTimes":6.0,
                                 "calledTimes":6.0,
                                 "smsNotifications":'',
                                 "activeShortest":2.0,
                                 "activeLongest":10888.0,
                                 "activeAverage":3377.0,

                                 "month":"201612"
                             },
                             "M2":{
                                 "month":"201611"
                             },
                             "M3":{
                                 "month":"201610"
                             },
                             "M4":{
                                 "distributionOfContacts":
                                     {
                                         "2":"3",
                                         "1":"4"
                                     },
                                 "dailyCallTimes":0.334,
                                 "hourStat":{
                                     "night":0,
                                     "day":10,
                                     "morning":0
                                 },
                                 "callTimes":8.0,
                                 "calledTimes":2.0,
                                 "smsNotifications":'',
                                 "activeShortest":6.0,
                                 "activeLongest":59391.0,
                                 "activeAverage":9786.223,
                                 "contactAmount":20.0,
                                 "month":"201609"
                             },
                             "M5":{
                                 "distributionOfContacts":{
                                     "3":"2",
                                     "2":"11",
                                     "1":"18",
                                     "10":"1",
                                     "6":"1",
                                     "5":"1"
                                 },
                                 "dailyCallTimes":2.162,
                                 "hourStat":{
                                     "night":6,
                                     "day":55,
                                     "morning":6
                                 },
                                 "callTimes":38.0,
                                 "calledTimes":29.0,
                                 "smsNotifications":'',
                                 "activeShortest":2.0,
                                 "activeLongest":156909.0,
                                 "activeAverage":10155.107,
                                 "contactAmount":30.0,
                                 "month":"201608"
                             },
                             "T6":{
                                 "distributionOfContacts":{
                                     "3":"3",
                                     "2":"14",
                                     "1":"17",
                                     "7":"1",
                                     "5":"1",
                                     "11":"1"
                                 },
                                 "dailyCallTimes":0.446,
                                 "hourStat":{
                                     "night":6,
                                     "day":65,
                                     "morning":6
                                 },
                                 "callTimes":46.0,
                                 "calledTimes":31.0,
                                 "smsNotifications":'',
                                 "activeShortest":2.0,
                                 "activeLongest":156909.0,
                                 "activeAverage":10876.54,
                                 "contactAmount":37.0,
                                 "month":"halfyear"
                             }
                         },
            "18989821092__a":
            {
                             "M0":
                              {"distributionOfContacts":{
                                  "3":"1",
                                  "2":"13",
                                  "1":"16",
                                  "10":"1",
                                  "7":"1",
                                  "6":"2",
                                  "4":"3",
                                  "22":"1",
                                  "36":"1",
                                  "8":"1",
                                  "13":"2"
                              },
                                  "dailyCallTimes":8.901,
                                  "hourStat":{
                                      "night":6,
                                      "day":158,
                                      "morning":14
                                  },
                                  "callTimes":75.0,
                                  "calledTimes":103.0,
                                  "smsNotifications":'',
                                  "activeShortest":1.0,
                                  "activeLongest":79236.0,
                                  "activeAverage":9615.126,
                                  "contactAmount":42.0,
                                  "month":"201701"
                              },
                             "M1":{
                                 "distributionOfContacts":{
                                     "3":"1",
                                     "5":"1",
                                     "4":"1"
                                 },
                                 "dailyCallTimes":0.388,
                                 "hourStat":{
                                     "night":0,
                                     "day":12,
                                     "morning":0
                                 },
                                 "callTimes":6.0,
                                 "calledTimes":6.0,
                                 "smsNotifications":'',
                                 "activeShortest":2.0,
                                 "activeLongest":10888.0,
                                 "activeAverage":3377.0,
                                 "contactAmount":4.0,
                                 "month":"201612"
                             },
                             "M2":{
                                 "month":"201611"
                             },
                             "M3":{
                                 "month":"201610"
                             },
                             "M4":{
                                 "distributionOfContacts":
                                     {
                                         "2":"3",
                                         "1":"4"
                                     },
                                 "dailyCallTimes":0.334,
                                 "hourStat":{
                                     "night":0,
                                     "day":10,
                                     "morning":0
                                 },
                                 "callTimes":8.0,
                                 "calledTimes":2.0,
                                 "smsNotifications":'',
                                 "activeShortest":6.0,
                                 "activeLongest":59391.0,
                                 "activeAverage":9786.223,
                                 "contactAmount":7.0,
                                 "month":"201609"
                             },
                             "M5":{
                                 "distributionOfContacts":{
                                     "3":"2",
                                     "2":"11",
                                     "1":"18",
                                     "10":"1",
                                     "6":"1",
                                     "5":"1"
                                 },
                                 "dailyCallTimes":2.162,
                                 "hourStat":{
                                     "night":6,
                                     "day":55,
                                     "morning":6
                                 },
                                 "callTimes":38.0,
                                 "calledTimes":29.0,
                                 "smsNotifications":'',
                                 "activeShortest":2.0,
                                 "activeLongest":156909.0,
                                 "activeAverage":10155.107,
                                 "contactAmount":34.0,
                                 "month":"201608"
                             },
                             "T6":{
                                 "distributionOfContacts":{
                                     "3":"3",
                                     "2":"14",
                                     "1":"17",
                                     "7":"1",
                                     "5":"1",
                                     "11":"1"
                                 },
                                 "dailyCallTimes":0.446,
                                 "hourStat":{
                                     "night":6,
                                     "day":65,
                                     "morning":6
                                 },
                                 "callTimes":46.0,
                                 "calledTimes":31.0,
                                 "smsNotifications":'',
                                 "activeShortest":2.0,
                                 "activeLongest":156909.0,
                                 "activeAverage":10876.54,
                                 "contactAmount":30.0,
                                 "month":"halfyear"
                             }
                         },
            "13820019795_8a404758b8f8b87c70006b8e9f4614db_":
            {
                            "M0":{
                                "distributionOfContacts":{
                                    "3":"1",
                                    "2":"13",
                                    "1":"16",
                                    "10":"1",
                                    "7":"1",
                                    "6":"2",
                                    "4":"3",
                                    "22":"1",
                                    "36":"1",
                                    "8":"1",
                                    "13":"2"
                                },
                                "dailyCallTimes":8.901,
                                "hourStat":{
                                    "night":6,
                                    "day":158,
                                    "morning":14
                                },
                                "callTimes":75.0,
                                "calledTimes":103.0,
                                "smsNotifications":'',
                                "activeShortest":1.0,
                                "activeLongest":79236.0,
                                "activeAverage":9615.126,
                                "contactAmount":19.0,
                                "month":"201701"
                            },
                            "M1":{
                                "distributionOfContacts":{
                                    "3":"1",
                                    "5":"1",
                                    "4":"1"
                                },
                                "dailyCallTimes":0.388,
                                "hourStat":
                                    {"night":0,
                                     "day":12,
                                     "morning":0
                                     },
                                "callTimes":6.0,
                                "calledTimes":6.0,
                                "smsNotifications":'',
                                "activeShortest":2.0,
                                "activeLongest":10888.0,
                                "activeAverage":3377.0,
                                "contactAmount":3.0,
                                "month":"201612"
                            },
                            "M2":{
                                "month":"201611"
                            },
                            "M3":{
                                "month":"201610"
                            },
                            "M4":{
                                "distributionOfContacts":{
                                    "2":"3","1":"4"
                                },
                                "dailyCallTimes":0.334,
                                "hourStat":{
                                    "night":0,
                                    "day":10,
                                    "morning":0
                                },
                                "callTimes":8.0,
                                "calledTimes":2.0,
                                "smsNotifications":'',
                                "activeShortest":6.0,
                                "activeLongest":59391.0,
                                "activeAverage":9786.223,
                                "contactAmount":7.0,
                                "month":"201609"
                            },
                            "M5":{
                                "distributionOfContacts":{
                                    "3":"2",
                                    "2":"11",
                                    "1":"18",
                                    "10":"1",
                                    "6":"1",
                                    "5":"1"
                                },
                                "dailyCallTimes":2.162,
                                "hourStat":{
                                    "night":6,
                                    "day":55,
                                    "morning":6
                                },
                                "callTimes":38.0,
                                "calledTimes":29.0,
                                "smsNotifications":'',
                                "activeShortest":2.0,
                                "activeLongest":156909.0,
                                "activeAverage":10155.107,

                                "month":"201608"
                            },
                            "T6":{
                                "distributionOfContacts":{
                                    "3":"3",
                                    "2":"14",
                                    "1":"17",
                                    "7":"1",
                                    "5":"1",
                                    "11":"1"
                                },
                                "dailyCallTimes":0.446,
                                "hourStat":{"night":6,
                                            "day":65,
                                            "morning":6
                                            },
                                "callTimes":46.0,
                                "calledTimes":31.0,
                                "smsNotifications":'',
                                "activeShortest":2.0,
                                "activeLongest":156909.0,
                                "activeAverage":10876.54,
                                "contactAmount":37.0,
                                "month":"halfyear"
                            }
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
}




class TestPlugin(unittest.TestCase):

    def setUp(self):
        self.data = data['trustutn_loan_phone']
        self.tel_number = data['apply_base']['mobile']

    def test_mobile_activeness(self):
        handler = Handle(self.data, self.tel_number)
        res = handler.handle()
        print res


if __name__ == '__main__':
    unittest.main()
