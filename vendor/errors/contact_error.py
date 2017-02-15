# -*- coding: utf-8 -*-

from vendor.errors.common import ServerError
from vendor.messages.response_code import ResponseCode


class ClientCodeInexistence(ServerError):
    status = ResponseCode.UNAVAILABLE_CLIENT_CODE
    message = ResponseCode.message(status)

