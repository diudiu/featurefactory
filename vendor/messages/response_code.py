# -*- coding: utf-8 -*-


class ResponseCode(object):
    """
        define for various code for response status
    """
    FAILED = 0
    SUCCESS = 1

    SERVER_BUSY = 5000

    DATABASE_ERROR = 40101

    RESPONSE_MESSAGE = {
        FAILED: u"操作失败",
        SUCCESS: u"操作成功",

        SERVER_BUSY: u"服务器繁忙，请稍后重试！",

        DATABASE_ERROR: u"数据库服务错误",
    }

    @classmethod
    def message(cls, status):
        return cls.RESPONSE_MESSAGE.get(status, u'')
