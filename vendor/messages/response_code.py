# -*- coding: utf-8 -*-


class ResponseCode(object):
    """
        define for various code for response status
    """
    FAILED = 0
    SUCCESS = 1

    RESPONSE_MESSAGE = {

    }

    @classmethod
    def message(cls, status):
        return cls.RESPONSE_MESSAGE.get(status, u'')
