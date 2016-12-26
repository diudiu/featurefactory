# -*- coding:utf-8 -*-
"""
    Copyright (c) 2013-2016 SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.JunPeng
    Date:  2016/12/22
    Change Activity:

"""
import json

from vendor.utils.encrypt import Cryption
from apps.common.models import ClientOverview
from apps.remote.models import FeatureFieldRel


class Judger(object):
    """
        1.身份验证
        2.数据解密
        3.参数可用性验证
        4.异常抛出

        # is client code useful and get messages belong to this client
        #
        # decrypt the messages
        # data = Cryption.aes_base64_decrypt(post_data['content'], des_key)
        # message = json.loads(data)
        #
        # get target keys and arguments, check them in the DB
        #
        # packing the useful messages go to the next part of the syetem
    """

    def __init__(self, client_code, data):
        self.client_code = client_code
        self.client_id = ''
        self.client_secret = ''
        self.des_key = ''
        self.origin_data = data
        self.cryption = Cryption()
        self.apply_id = ''
        self.target_features = []
        self.arguments = {}
        self.ret_msg = []

    def _check_sum(self):
        if self.client_id and self.client_secret and self.des_key and self.target_features and self.arguments \
                and (len(self.target_features) == len(self.ret_msg)):
            return True
        else:
            return False

    def _check_identity(self):
        client_package = ClientOverview.objects.filter(client_code=self.client_code)
        if not client_package:
            raise  # E02
        client_package = client_package[0]
        self.client_id = client_package.client_id
        self.client_secret = client_package.client_secret
        self.des_key = client_package.des_key

    def _decrypt(self):
        try:
            json_data = Cryption.aes_base64_decrypt(self.origin_data, self.des_key)
            message = json.loads(json_data)
        except Exception as e:
            raise  # E03
        self.apply_id = message.get('apply_id', None)
        self.target_features = message.get('res_keys', None)
        self.arguments = message.get('arguments', None)
        self.arguments.update({
            'apply_id': self.apply_id
        })
        if not self.apply_id:
            raise  # E04
        if not self.target_features:
            raise  # E05
        if not self.arguments:
            raise  # E06

    def _args_useful_check(self):
        """
        need sql which mapping the target features and arguments
        :return:
        """

        arg_msg_list = FeatureFieldRel.objects.filter(
            feature_name__in=self.target_features,
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
                raise

    def work_stream(self):
        self._check_identity()
        self._decrypt()
        self._args_useful_check()
        return self._check_sum()
