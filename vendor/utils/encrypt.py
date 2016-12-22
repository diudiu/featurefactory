# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH(Shaohan Niu), All Rights Reserved.
    -----------------------------------------------------------
    Author:
    Date:  2016/12/22
    Change Activity:

"""

import os
import base64
import json

import pyDes
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5 as pk
from Crypto.Cipher import DES
from Crypto.Cipher import AES


class Cryption(object):
    """
        encrypt and decrypt
    """
    block_size = DES.block_size
    UTILS_DIR = os.path.dirname(__file__)
    lkl_public_key = RSA.importKey(open(UTILS_DIR + '/keys/lkl_rsa_public_key.pem', 'r').read())
    public_key = RSA.importKey(open(UTILS_DIR + '/keys/rsa_public_key.pem', 'r').read())
    pkcs8_private_key = RSA.importKey(open(UTILS_DIR + '/keys/pkcs8_rsa_private_key.pem', 'r').read())
    pad_str = ['\x01', '\x02', '\x03', '\x04', '\x05', '\x06', '\x07', '\x08']

    @classmethod
    def des_base64_encrypt(cls, reqdata, des_key):
        """ 基于DES和base64的加密算法
            @:param reqdata 需要加密的请求数据
            @:param key des加密的密钥
        """
        if not isinstance(reqdata, str):
            reqdata = json.dumps(reqdata)
        # key = des_key
        length = len(reqdata)
        if length < cls.block_size:
            add = cls.block_size - length
        elif length > cls.block_size:
            add = cls.block_size - (length % cls.block_size)
        else:
            add = 8

        reqdata += cls.pad_str[add - 1] * add
        des = DES.new(des_key, DES.MODE_ECB)
        encrypt_data = des.encrypt(reqdata)

        return base64.b64encode(encrypt_data)

    @classmethod
    def des_base64_decrypt(cls, retdata, des_key):
        """DES解密
            @:param retdata: lakala reponse retData
        """
        # key = cls.des_key
        debase64_data = base64.b64decode(retdata)
        des = DES.new(des_key, DES.MODE_ECB)
        decrypt_data = des.decrypt(debase64_data)
        _strip = '|'.join(cls.pad_str)
        return decrypt_data.strip(_strip)

    @classmethod
    def rsa_sign(cls, des_reqdata):
        """
            @:param reqdata: request reqData
        """
        h = SHA.new(des_reqdata)
        signer = pk.new(cls.pkcs8_private_key)
        signature = signer.sign(h)

        return base64.b64encode(signature)

    @classmethod
    def check_rsa_sign(cls, des_retdata, sign):
        """ check lakala sign use this method
            @:param retdata: lakala response retData
            @:param sign: lakala response sign
        """
        # retdata = base64.b64decode(des_retdata)
        sign = base64.b64decode(sign)
        h = SHA.new(des_retdata)
        verifier = pk.new(cls.lkl_public_key)
        # verifier = pk.new(cls.public_key)

        return verifier.verify(h, sign)

    @classmethod
    def des_base64_encrypt_cbc(cls, text, key, iv, code=''):
        """ 基于DES和base64的加密算法
            :param text 国政通的加密串须使用GBK编码
            :param key des加密的密钥
            :param iv des的向量
            :param code text加密时的编码
        """
        # 对text进行转码 --> GBK
        if code and isinstance(text, str):
            text = text.decode('utf-8').encode(code)
        elif code and isinstance(text, unicode):
            text = text.encode(code)
        else:
            text = text.encode('utf-8')
        des = pyDes.des(key, pyDes.CBC, iv, padmode=pyDes.PAD_PKCS5)
        encrypt_text = des.encrypt(text)
        return base64.encodestring(encrypt_text).strip()

    @classmethod
    def des_base64_decrypt_cbc(cls, text, key, iv, code=''):
        """ 基于DES和base64的解密算法
            :param code:
            :param text 解密的文本
            :param key des加密的密钥
            :param iv des的向量
        """
        des = pyDes.des(key, pyDes.CBC, iv, padmode=pyDes.PAD_PKCS5)
        decode_text = des.decrypt(base64.decodestring(text))
        if code:
            decode_text = decode_text.decode(code).encode('utf-8')
        else:
            decode_text = decode_text.encode('utf-8')
        return decode_text

    @classmethod
    def aes_base64_encrypt(cls, text, key, iv='1234567890123456'):
        """
        aes加密, MODE_CBC, key, IV
        """
        if isinstance(text, unicode):
            text = text.encode('utf-8')
        aes_encrypt = AES.new(key, mode=AES.MODE_CBC, IV=iv)
        pad = lambda s: s + (AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size)
        text = pad(text)
        encrypt_text = aes_encrypt.encrypt(text)
        return base64.b64encode(encrypt_text)

    @classmethod
    def aes_base64_decrypt(cls, text, key, iv='1234567890123456'):
        """
        aes解密, MODE_CBC, KEY, IV
        """
        try:
            aes_decrypt = AES.new(key, mode=AES.MODE_CBC, IV=iv)
            decode_text = base64.b64decode(text)
            decode_text = aes_decrypt.decrypt(decode_text)
            unpad = lambda s: s[0:-ord(s[-1])]
            decode_text = unpad(decode_text)
            return decode_text.decode('utf-8')
        except (UnicodeError, TypeError, ValueError, AssertionError, Exception) as e:
            return None
