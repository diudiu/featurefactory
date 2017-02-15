# -*- coding: utf-8 -*-
class MyException(Exception):
    """ define Exception message """
    status = 999999
    message = "error"

    def __init__(self, status=None, message=None):
        if message:
            self.message = message
        if status:
            self.status = status
        super(MyException, self).__init__(self.status, self.message)
