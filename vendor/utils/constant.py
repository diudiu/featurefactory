# -*- coding:utf-8 -*-

"""
    All constants used in the system.
"""


class Constant(object):

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstantError, "Can't change constant.{name}".format(name)

        if not name.isupper():
            raise self.ConstCaseError, 'constant name "{name}" is not all uppercase'.format(name)

        self.__dict__[name] = value

    def __getattr__(self, item):
        try:
            return self.__dict__[item]
        except KeyError:
            return None

cons = Constant()

CACHE_TIMEOUT = 86400

cons.STR_EMPTY = ''
cons.ZERO = 0
cons.COMMA = ','
cons.SEMICOLON = ';'
cons.BLANK = ' '
cons.APPLY_ID = 'apply_id'
cons.CLIENT_CODE = 'client_code'
cons.CLIENT_ID = 'client_id'
cons.CLIENT_SECRET = 'client_secret'
cons.DES_KEY = 'des_key'

cons.RESPONSE_REQUEST_STATUS = 'status'
cons.RESPONSE_REQUEST_MESSAGE = 'message'
cons.RESPONSE_REQUEST_RES_DATA = 'res_data'
cons.RESPONSE_HANDLE_RESULT = 'result'
cons.RESPONSE_HANDLE_MESSAGE = 'result_message'
cons.RESPONSE_HANDLE_CONTENT = 'content'

cons.PROTOCOL_HTTP = 'http'
cons.PROTOCOL_HTTPS = 'https'
cons.PROTOCOL_SYS_LOCAL = 'local'
cons.REQUEST_PROTOCOL_TYPE = (
    (cons.PROTOCOL_HTTP, cons.PROTOCOL_HTTP),
    (cons.PROTOCOL_HTTPS, cons.PROTOCOL_HTTPS),
    (cons.PROTOCOL_SYS_LOCAL, cons.PROTOCOL_SYS_LOCAL),
)

cons.CALL_DATA_SOURCE_REMOTE = 'REMOTE'
cons.CALL_DATA_SOURCE_LOCAL = 'LOCAL'
cons.CALL_DATA_SOURCE_TYPE = [
    (cons.CALL_DATA_SOURCE_REMOTE, u'远程接口调用'),
    (cons.CALL_DATA_SOURCE_BUSINESS, u'本地调用')
]

cons.HTTP_GET = 'GET'                                              # http GET
cons.HTTP_POST = 'POST'                                            # http POST
cons.LOCAL_REQUEST = 'LOCAL'
cons.HTTP_METHOD = (
    (cons.HTTP_GET, cons.HTTP_GET),
    (cons.HTTP_POST, cons.HTTP_POST),
    (cons.LOCAL_REQUEST, cons.LOCAL_REQUEST),
)

cons.UNICOM_MOBILE_NUMBER = 'UMN'
cons.UNICOM_MATCH_STR = '(^1(3[0-2]|4[5]|5[56]|7[6]|8[56])\\d{8}$)|(^1709\\d{7}$)'

cons.YD_MOBILE_NUMBER = 'YMN'
cons.YD_MATCH_STR = '(^1(3[4-9]|4[7]|5[0-27-9]|7[8]|8[2-478])\\d{8}$)|(^1705\\d{7}$)'

cons.TELECOME_MOBILE_NUMBER = 'TMN'
cons.TELECOME_MATCH_STR = '^1((33|53|77|8[019])[0-9]|349)|(700\\d{7}$)'

cons.OTHER_MOBILE_NUMBER = 'OMN'

cons.LP_BASE_HANDLE = 'studio.lp_dataocean_handle'
cons.HANDLE_CLASS = 'Handle'
cons.HANDLE_COMBINE = '.'

# Arithmetic type
cons.ARITHMETIC_LEFT_CLOSE_RIGHT_OPEN = "LEFT-CLOSE-RIGHT-OPEN"
cons.ARITHMETIC_LEFT_OPEN_RIGHT_CLOSE = "LEFT-OPEN-RIGHT-CLOSE"
