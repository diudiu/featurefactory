# -*- coding: utf-8 -*-

from vendor.messages.response_code import ResponseCode


class ServerError(Exception):
    """ define server error, most need notice monitor """
    status = ResponseCode.SERVER_BUSY
    message = ResponseCode.RESPONSE_MESSAGE[status]

    def __init__(self, message=None):
        if not message:
            message = self.message

        self.message = message
        super(ServerError, self).__init__(message)


class DatabaseError(ServerError):
    status = ResponseCode.DATABASE_ERROR
    message = ResponseCode.RESPONSE_MESSAGE[status]
