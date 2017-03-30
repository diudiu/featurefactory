# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH(Shaohan Niu), All Rights Reserved.
    -----------------------------------------------------------
    Author:
    Date:  2016/12/22
    Change Activity:

"""


import base64
from Crypto.Cipher import AES


class Cryption(object):
    """
        encrypt and decrypt
    """

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
