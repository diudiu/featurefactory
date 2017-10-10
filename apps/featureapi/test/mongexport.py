# -*- coding:utf-8 -*-

import os
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
for i in data_identity.keys():
    req="do_%s_request" % i
    res = "do_%s_response" % i
    print req, res
    req_ex = "mongoexport -h 10.31.34.133 -u dataocean  -p Syph@dataocean -d dataocean -c %s -o /tmp/gyftmp/%s.json" % (req,req)
    res_ex = "mongoexport -h 10.31.34.133 -u dataocean  -p Syph@dataocean -d dataocean -c %s -o /tmp/gyftmp/%s.json" % (res,res)
    req_im = "mongoimport -h 10.31.34.133 -u dataocean_debug  -p Syph@dataocean_debug -d dataocean_debug -c %s  /tmp/gyftmp/%s.json" % (
    req, req)
    res_im = "mongoimport -h 10.31.34.133 -u dataocean_debug  -p Syph@dataocean_debug -d dataocean_debug -c %s  /tmp/gyftmp/%s.json" % (
    res, res)
    print req_ex
    print req_im
    print res_ex
    print res_im

    os.system(req_ex)
    os.system(req_im)
    os.system(res_ex)
    os.system(res_im)
