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

from apps.etl.models import FeatureProcessInfo
from apps.etl.context import ProcessContext
from apps.etl.factory import *

logger = logging.getLogger('apps.etl')


class Fabricate(object):

    def __init__(self, origin_data, base_data, apply_id):
        self.origin_data = origin_data
        self.base_data = base_data
        self.apply_id = apply_id
        self.ret_value = {}
        self.keys_map = {data['target_field_name']: data['data_identity'] for data in base_data}
        self.keys_list = self.keys_map.keys()
        self.process_base = ProcessContext(self.apply_id)

    def fabricate(self):
        feature_prams = FeatureProcessInfo.objects.filter(
            feature_name__in=self.keys_list,
            is_delete=False
        )
        for feature_pram in feature_prams.iterator():
            data = self.origin_data[feature_pram.data_identity]
            data.update({
                'data_identity': feature_pram.data_identity
            })
            f_factory = Factory(data)
            factory = f_factory(feature_pram.process_type, feature_pram.feature_name)
            machine = factory.machine
            # value = machine
            value = machine.dispose_data()
            self.ret_value.update({
                feature_pram.feature_name: value
            })
        return self.ret_value

    def process_data_2_storage(self):
        self.process_base.kwargs.update(self.ret_value)
        self.process_base.save()
        return True
