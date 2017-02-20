# -*- coding:utf-8 -*-

import abc


class GrantCreditAbstract(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def grant(self):
        """ grant credit limits by the pre grant credit model """

    @abc.abstractmethod
    def pre_process(self):
        """ pre process """
