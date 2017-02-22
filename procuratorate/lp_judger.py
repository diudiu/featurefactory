# -*- coding:utf-8 -*-
"""
    Copyright (c) 2013-2016 SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.JunPeng
    Date:  2016/12/22
    Change Activity:

"""
import logging

from apps.etl.models import FeatureConf
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
        self.feature_list = []
        self.ret_msg = []
        self.arguments = []

    def work_stream(self):
        self._fill_attributes()
        base_data = {
            'client_code': self.client_code,
            'callback_url': self.callback_url,
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
            raise CallBackUrlMissing
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
            except (NameError, SyntaxError) as e:
                raise
            self.ret_msg.append({single_conf.feature_name: feature_conf})

    def _load_args(self):
        apply_data = ApplyContext(self.apply_id).load()
        self.proposer_id = apply_data.get('proposer_id', None)
        if not self.proposer_id:
            raise
        portrait_data = PortraitContext(self.proposer_id).load()

