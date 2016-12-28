# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH(Shaohan Niu), All Rights Reserved.
    -----------------------------------------------------------
    Author: S.JunPeng
    Date:  2016/12/26
    Change Activity:

"""

import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'featurefactory.settings')
import django
django.setup()

from apps.common.models import ClientOverview


def client_overview_msg():
    messages = [
        {
            'client_code': 'lp_test',
            'client_id': 'eezqKVwe3Fzc72m3K6LzfK4CbJDb7hbtoJThzsBo',
            'client_secret': '5yr2oMcUQSzld9JifoMvkN8tmyiwIB9Ra9IxUDDlmDmlPx3V8uJRkiTpSvVUdRVHLA1F91iyxgP4riz4fWVMbbyfq3ovo1c9kzwHtDrtMqVpMd2vZPFXGAkh7IjuBDQT',
            'des_key': 'yyyyyyuuuuoooooo',
        },
    ]
    return messages


def add_client_overview():
    messages = client_overview_msg()
    for msg in messages:
        if ClientOverview.objects.filter(client_code=msg['client_code']).count() > 0:
            continue
        else:
            cov = ClientOverview(
                client_code=msg['client_code'],
                client_id=msg['client_id'],
                client_secret=msg['client_secret'],
                des_key=msg['des_key']
            )
            cov.save()
