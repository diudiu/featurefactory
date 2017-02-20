# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.JunPeng
    Date:  2016/12/26
    Change Activity:
"""
import logging
import time

from apps.etl.context import CacheContext, ArgsContext
from apps.datasource.models import InterfaceFieldRel, DsInterfaceInfo

logger = logging.getLogger('apps.remote')


class DataPrepare(object):

    def __init__(self, data_identity, apply_id):
        self.data_identity = data_identity
        self.apply_id = apply_id
        self.cache_base = CacheContext(self.apply_id)
        self.argument_base = ArgsContext(self.apply_id)
        self.parm_keys = []
        self.parm_dict = {}

    def get_original_data(self):

        ret_data = self.get_data_from_db()
        if not ret_data:
            ret_data = self.get_data_from_interface()
        if not ret_data:
            raise
        return ret_data

    def get_data_from_db(self):
        ret_data = {}
        data = self.cache_base.get(self.data_identity)
        if data:
            ret_data.update({
                self.data_identity: data[self.data_identity]
            })
        return ret_data

    def get_data_from_interface(self):
        ds_conf = DsInterfaceInfo.objects.filter(
            data_identity=self.data_identity,
            is_delete=False
        )[0]
        if not ds_conf:
            raise
        self.prepare_parms()
        url = ds_conf.data_source.backend_url + ds_conf.route
        data_prams = eval(ds_conf.must_data % self.parm_dict)
        origin_data = self.do_request(url, data_prams)
        if not origin_data:
            raise  # TODO get data error
        self.cache_base.kwargs.update({
            self.data_identity: {
                'origin_data': origin_data,
                'prams': self.parm_dict,
            }
        })
        self.cache_base.save()
        return {self.data_identity: origin_data}

    def prepare_parms(self):
        parm_conf = InterfaceFieldRel.objects.filter(
            data_identity=self.data_identity,
            is_delete=False
        )
        if not parm_conf:
            raise
        self.parm_keys = [conf.raw_field_name for conf in parm_conf]
        arguments = self.argument_base.load()
        for key in self.parm_keys:
            value = arguments.get(key, None)
            if not value:
                raise
            self.parm_dict.update({
                key: value
            })

    def do_request(self, url, data):
        # json_data = json.dumps(data, encoding="UTF-8", ensure_ascii=False)
        # response = requests.post(url, json_data)
        # content = response.content
        # content = json.loads(content)
        result = {'time': time.ctime(time.time())}
        return result
