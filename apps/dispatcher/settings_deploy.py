# -*- coding:utf-8 -*-
import os
URL_1_0_APPLY = "http://" + os.getenv('RISKCTL_1', '') + "/api/credit/apply/"
URL_1_0_CALLBACK = "http://" + os.getenv('RISKCTL_1', '') + "/api/async/callback/"
URL_1_0_RESULT = "http://" + os.getenv('RISKCTL_1', '') + "/api/credit/result/"


URL_2_0_FORMAL = "http://" + os.getenv('RISKCTL_2_DE', '') + "/syph-re/api/credit/apply/async/formal/"
URL_2_0_BANKCARD = "http://" + os.getenv('RISKCTL_2_DE', '') + "/syph-re/api/credit/apply/async/bankcard/"
URL_2_0_EMAIL = "http://" + os.getenv('RISKCTL_2_DE', '') + "/syph-re/api/credit/apply/async/email/"
URL_2_0_ZM = "http://" + os.getenv('RISKCTL_2_DE') + "/syph-re/api/credit/apply/async/aliZmCredit/"
URL_2_0_GJJ = "http://" + os.getenv('RISKCTL_2_DE') + "/syph-re/api/credit/apply/async/accumulation/"
URL_2_0_OPERATOR = "http://" + os.getenv('RISKCTL_2_DE', '') + "/syph-re/api/credit/apply/async/operator/"
URL_2_0_FINAL = "http://" + os.getenv('RISKCTL_2_DE', '') + "/syph-re/api/credit/apply/async/final/"


URL_RECEIVE = "http://" + os.getenv('RISKCTL_2_FF', '') + "/api/async/result/"

HEADERS = {
    "Content-type": "application/json; charset=utf-8",
}
