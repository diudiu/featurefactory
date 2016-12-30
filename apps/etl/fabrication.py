# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH(Shaohan Niu), All Rights Reserved.
    -----------------------------------------------------------
    Author: S.JunPeng
    Date:  2016/12/26
    Change Activity:
"""
from apps.etl.models import FeatureProcessInfo
from apps.etl.factory import *


def fabricate(origin_data, base_data):
    keys_map = {data['target_field_name']: data['data_identity'] for data in base_data}
    keys_list = keys_map.keys()
    ret_value = {}
    feature_prams = FeatureProcessInfo.objects.filter(
        feature_name__in=keys_list,
        is_delete=False
    )
    for feature_pram in feature_prams.iterator():
        data = origin_data[feature_pram.data_identity]
        data.update({
            'data_identity': feature_pram.data_identity
        })
        f_factory = Factory(data)
        factory = f_factory(feature_pram.process_type, feature_pram.feature_name)
        machine = factory.machine
        # value = machine
        value = machine.dispose_data()
        ret_value.update({
            feature_pram.feature_name: value
        })
    return ret_value
