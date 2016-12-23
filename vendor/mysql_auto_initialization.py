# -*- coding: utf-8 -*-

import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'featurefactory.settings')
import django
django.setup()

from apps.common.models import ClientOverview


def client_overview_msg():
    # client_code = models.CharField(u'', max_length=128)
    # client_id = models.CharField(u'', max_length=128)
    # client_secret = models.CharField(u'', max_length=256)
    # res_key = models.CharField(u'', max_length=128)
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

if __name__ == '__main__':
    add_client_overview()
