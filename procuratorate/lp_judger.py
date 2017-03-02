# -*- coding:utf-8 -*-
"""
    Copyright (c) 2013-2016 SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.JunPeng
    Date:  2016/12/22
    Change Activity:

"""
import logging
from jsonpath_rw_ext import parse

from apps.etl.models import FeatureConf, PreFieldInfo
from apps.etl.context import ApplyContext, ArgsContext, PortraitContext
from vendor.errors.api_errors import *

logger = logging.getLogger('apps.featureapi')


class Judger(object):
    """

    """

    def __init__(self, content, client_code):
        if not client_code:
            raise ClientCodeMissing
        self.content = content
        self.client_code = client_code
        self.apply_id = ''
        self.proposer_id = ''
        self.callback_url = ''
        self.async = True
        self.feature_list = []
        self.ret_msg = {}
        self.arguments = {}

    def work_stream(self):
        self._fill_attributes()
        base_data = {
            'client_code': self.client_code,
            'callback_url': self.callback_url,
            'is_async': self.async,
            'apply_id': self.apply_id,
            'proposer_id': self.proposer_id,
            'feature_conf': self.ret_msg,
            'base_args': self.arguments
        }
        return base_data

    def _fill_attributes(self):
        self.apply_id = self.content.get('apply_id', None)
        self.callback_url = self.content.get('callback_url', None)
        if not self.callback_url:
            self.async = False
        self.feature_list = self.content.get('res_keys', None)
        self._load_conf()
        if not self.ret_msg:
            logger.error(
                'Response from the function of `judge._decrypt`, error_msg=%s, rel_err_msg=%s, apply_id=%s'
                % (GetArgumentsError.message, "Missing arguments in the post_data", self.apply_id),
                exc_info=True
            )
            raise GetArgumentsError  # E06
        self._load_args()

    def _load_conf(self):
        full_conf = FeatureConf.objects.filter(
            feature_name__in=self.feature_list,
            is_delete=False
        )
        if full_conf.count() != len(self.feature_list):
            raise  # TODO 配置有误 数量对不上

        for single_conf in full_conf.iterator():
            try:
                feature_conf = eval(single_conf.raw_field_name)
                feature_conf.update({
                    'collect_type': single_conf.collect_type
                })
            except (NameError, SyntaxError) as e:
                raise
            self.ret_msg.update({single_conf.feature_name: feature_conf})

    def _load_args(self):
        arg_base = ArgsContext(self.apply_id)
        self.arguments = arg_base.load()
        if not self.arguments:
            self.arguments = {}
            apply_data = ApplyContext(self.apply_id).load()
            self.proposer_id = apply_data.get('proposer_id', None)
            if not self.proposer_id:
                raise ProposerIdMissing
            portrait_data = PortraitContext(self.proposer_id).load()
            if not portrait_data:
                raise NoPortraitData
            pre_conf = PreFieldInfo.objects.filter(
                is_delete=False
            )
            full_data = {
                'apply_data': apply_data,
                'portrait_data': portrait_data
            }
            for pre in pre_conf:
                self.arguments.update({
                    pre.field_name: self.get_value(full_data[pre.source], pre.path)
                })
            arg_base.kwargs.update(self.arguments)
            arg_base.save()

    @staticmethod
    def get_value(data, path):
        path_expr = parse(path)
        temp = path_expr.find(data)
        result = []
        for val in temp:
            result.append(val.value)
        if result:
            return result[0]
        else:
            return None
