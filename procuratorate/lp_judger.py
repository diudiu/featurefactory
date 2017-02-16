# -*- coding:utf-8 -*-
"""
    Copyright (c) 2013-2016 SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.JunPeng
    Date:  2016/12/22
    Change Activity:

"""
import logging

from apps.remote.models import FeatureFieldRel
from apps.datasource.models import InterfaceFieldRel
from apps.etl.context import ApplyContext
from apps.etl.context import PortraitContext
from vendor.errors.api_errors import *

logger = logging.getLogger('apps.featureapi')


class Judger(object):
    """
        1.authentication (_check_identity)
        2.data decryption (_decrypt)
        3.check availability of arguments (_args_useful_check)
        4.throw the Exceptions
        5.finally check all works
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
        self.arguments = {}
        self.ret_msg = []

    def work_stream(self):
        self._fill_attributes()
        base_data = {
            'client_code': self.client_code,
            'callback_url': self.callback_url,
            'apply_id': self.apply_id,
            'feature_list': self.feature_list,
            'useful_args': self.ret_msg,
        }
        return base_data

    def _fill_attributes(self):
        self.apply_id = self.content.get('apply_id', None)
        self.callback_url = self.content.get('callback_url', None)
        if not self.callback_url:
            raise CallBackUrlMissing
        self.feature_list = self.content.get('res_keys', None)
        apply_base = ApplyContext(self.apply_id)
        apply_data = apply_base.load()
        self.proposer_id = apply_data.get('proposer_id', None)
        if not self.proposer_id:
            raise ProposerIdMissing

        portrait_base = PortraitContext(self.proposer_id)
        portrait_data = portrait_base.load()
        self._prepare_args(apply_data, portrait_data)
        if not self.arguments:
            logger.error(
                'Response from the function of `judge._decrypt`, error_msg=%s, rel_err_msg=%s, apply_id=%s'
                % (GetArgumentsError.message, "Missing arguments in the post_data", self.apply_id),
                exc_info=True
            )
            raise GetArgumentsError  # E06
        feature_msg_list = FeatureFieldRel.objects.filter(
            feature_name__in=self.feature_list,
            is_delete=False,
        )
        data_identity_list = [feature.data_identity for feature in feature_msg_list]

        arg_msg_list = InterfaceFieldRel.objects.filter(
            data_identity__in=data_identity_list,
            is_delete=False
        ).order_by('data_identity')
        for arg_msg in arg_msg_list:
            if arg_msg.raw_field_name in self.arguments.keys():
                if self.ret_msg and (arg_msg.data_identity == (self.ret_msg[-1])['data_identity']):
                    sub_msg = self.ret_msg[-1]
                    sub_msg['arguments'].update({
                        arg_msg.raw_field_name: self.arguments[arg_msg.raw_field_name],
                    })
                    self.ret_msg[-1] = sub_msg
                else:
                    temp_msg = {
                        'data_identity': arg_msg.data_identity,
                        'arguments': {
                            arg_msg.raw_field_name: self.arguments[arg_msg.raw_field_name],
                        }
                    }
                    self.ret_msg.append(temp_msg)
            else:
                logger.info(
                    'Arguments are not enough to get all res_keys, \n filed_name=%s, apply_id=%s'
                    % (arg_msg.raw_field_name, self.apply_id)
                )
                logger.error(
                    'Response from the function of `judge._args_useful_check`, '
                    'error_msg=%s, rel_err_msg=%s, apply_id=%s'
                    % (ArgumentsAvailableError.message, "Arguments are not enough to get all res_keys", self.apply_id),
                    exc_info=True
                )
                raise ArgumentsAvailableError  # E07

    def _prepare_args(self, apply_data, portrait_data):
        self.arguments = portrait_data.get('data', None)
        self.arguments.update(apply_data.get('data', None))
