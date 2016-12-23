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
        self.appli_id = ''
        self.target_features = []
        self.arguments = {}

    def _check_sum(self):
        if self.client_id and self.client_secret and self.des_key and self.target_features and self.arguments:
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
        self.appli_id = message.get('apply_id', None)
        self.target_features = message.get('res_keys', None)
        self.arguments = message.get('arguments', None)
        if not self.appli_id:
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
        pass

    def work_stream(self):
        self._check_identity()
        self._decrypt()
        self._args_useful_check()
        if self._check_sum():
            pass
        else:
            pass
