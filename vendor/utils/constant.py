# -*- coding:utf-8 -*-

"""
    All constants used in the system.
"""


class Constant(object):
    class ConstantError(TypeError):
        pass

    class ConstantCaseError(ConstantError):
        pass

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

cons.STR_EMPTY = ''
cons.ZERO = 0
cons.COMMA = ','
cons.SEMICOLON = ';'
cons.BLANK = ' '

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


