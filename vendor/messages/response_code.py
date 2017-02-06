# -*- coding: utf-8 -*-


class ResponseCode(object):
    """
        define for various code for response status
    """
    FAILED = 0
    SUCCESS = 1

    SERVER_BUSY = 5000
    REQUEST_TYPE_ERROR = 30001
    USERS_IDENTIFICATION_ERROR = 30002
    INCOME_ENCRYPT_ERROR = 30003
    ARGUMENTS_UNAVAILABLE = 30004
    MISSING_APPLY_ID = 30010
    MISSING_RES_KEYS = 30011
    MISSING_ARGUMENTS = 30012

    DATABASE_ERROR = 40101

    RESPONSE_MESSAGE = {
        FAILED:                         u"操作失败",
        SUCCESS:                        u"操作成功",

        SERVER_BUSY:                    u"服务器繁忙，请稍后重试！",
        REQUEST_TYPE_ERROR:             u"请求方式错误, 请求数据应为JSON  请求方式应为HTTP-POST",
        USERS_IDENTIFICATION_ERROR:     u"用户身份不合法 client_code 错误或不存在",
        INCOME_ENCRYPT_ERROR:           u"数据解密错误, 传入参数加密错误",
        ARGUMENTS_UNAVAILABLE:          u'传入参数不足以获取所有目标特征, 请检查参数列表',
        MISSING_APPLY_ID:               u"传入数据内容缺失 apply_id",
        MISSING_RES_KEYS:               u"传入数据内容缺失 res_keys",
        MISSING_ARGUMENTS:              u"受信人输入数据缺失",

        DATABASE_ERROR:                 u"数据库服务错误",
    }

    @classmethod
    def message(cls, status):
        return cls.RESPONSE_MESSAGE.get(status, u'')
