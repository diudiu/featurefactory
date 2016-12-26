# -*- coding: utf-8 -*-

from vendor.errors.common import ServerError

from vendor.messages.response_code import ResponseCode


# E01
class RequestTypeError(AttributeError):
    status = ResponseCode.REQUEST_TYPE_ERROR,
    message = ResponseCode.message(status),

# E02


# E03


# E04


# E05


# E06
