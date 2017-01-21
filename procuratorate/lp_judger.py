# -*- coding:utf-8 -*-
"""
    Copyright (c) 2013-2016 SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.JunPeng
    Date:  2016/12/22
    Change Activity:

"""
import logging
import json

from apps.remote.models import FeatureFieldRel
from apps.etl.context import ApplyContext
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

    def __init__(self, content):
        self.content = content
        self.apply_id = ''
        self.feature_list = []
        self.arguments = {}
        self.ret_msg = []

    def work_stream(self):
        self._fill_attributes()
        base_data = {
            'apply_id': self.apply_id,
            'useful_args': self.ret_msg,
        }
        return base_data

    def _fill_attributes(self):
        self.apply_id = self.content.get('apply_id', None)
        self.feature_list = self.content.get('res_keys', None)
        apply_base = ApplyContext(self.apply_id)
        self.arguments = apply_base.load()

        if not self.arguments:
            logger.error('Response from the function of `judge._decrypt`, error_msg=%s, rel_err_msg=%s'
                         % (GetArgumentsError.message, "Missing arguments in the post_data"), exc_info=True)
            raise GetArgumentsError  # E06

        arg_msg_list = FeatureFieldRel.objects.filter(
            feature_name__in=self.feature_list,
            is_delete=False,
        )
        for arg_msg in arg_msg_list:
            if arg_msg.raw_field_name in self.arguments.keys():
                if self.ret_msg and (arg_msg.feature_name == (self.ret_msg[-1])['target_field_name']):
                    sub_msg = self.ret_msg[-1]

                    if arg_msg.feature_name == sub_msg['target_field_name']:
                        sub_msg['arguments'].update({
                            arg_msg.raw_field_name: self.arguments[arg_msg.raw_field_name],
                        })
                        self.ret_msg[-1] = sub_msg
                else:
                    temp_msg = {
                        'data_identity': arg_msg.data_identity,
                        'target_field_name': arg_msg.feature_name,
                        'arguments': {
                            arg_msg.raw_field_name: self.arguments[arg_msg.raw_field_name],
                        }
                    }
                    self.ret_msg.append(temp_msg)
            else:
                logger.error('Response from the function of `judge._args_useful_check`, error_msg=%s, rel_err_msg=%s'
                             % (ArgumentsAvailableError.message, "Arguments are not enough to get all res_keys"),
                             exc_info=True)
                raise ArgumentsAvailableError  # E07

    def _prepare_args(self):
        pass
