# -*- coding:utf-8 -*-
import pymongo
MONGO_HOST = '121.42.234.56'
MONGO_NAME = 'dataocean'
MONGO_USERNAME = 'dataocean'
MONGO_PASSWORD = 'Syph@dataocean'
MONGO_PORT = 27017

client = pymongo.MongoClient('121.42.234.56', 27017)
client['dataocean'].authenticate('dataocean', 'Syph@dataocean')
db = client['dataocean']

clients = pymongo.MongoClient('121.42.234.56', 27017)
clients['dataocean_debug'].authenticate('dataocean_debug', 'Syph@dataocean_debug')
dbs = client['dataocean_debug']

data_identity = {"bank_card_analysis_z": {"id_card_code": "411626199202213528"},
                 "bank_card_info_check3_z": {"id_card_code": "411626199202213528"},
                 "identity_verify_z": {"id_card_code": "411626199202213528"},
                 "mobile_identity_z": {"id_card_code": "411626199202213528"},
                 "shixin_zhixing_z": {"entity_id": "411626199202213528"},
                 "unicom_telecom_mobile_status_online_z": {"id_card_code": "411626199202213528"},
                 "yd_mobile_status_online_z": {"id_card_code": "411626199202213528"},
                 "agentg_black": {"id_card_code": "411626199202213528"},
                 "credit_card": {"bank_account": "6217900100011177162"},
                 "loan_agency": {"mobile": "13716315381"},
                 "personal_info": {"id_card_code": "411626199202213528"},
                 "geo_location": {},
                 "mobile_locale": {},
                 "crawler_email": {},
                 "jigour_black": {},
                 }
deal_identifying_list =[]
for d_identity, value in data_identity.iteritems():
    key = value.keys()[0]
    p = value.values()[0]
    collect = getattr(db, "do_%s_request" % d_identity)
    res = collect.find({"req_param.%s" % key: p})
    for i in res:
        deal_identifying = i["deal_identifying"]
        deal_identifying_list.append(deal_identifying.encode("utf8"))
