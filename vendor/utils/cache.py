# -*- coding:utf-8 -*-
"""
    Copyright (c) 2013-2016 SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: S.JunPeng
    Date:  2016/12/22
    Change Activity:

"""

import redis

from featurefactory.settings import REDIS_CONFIG

CACHE_TIMEOUT = 86400


class RedisX(object):

    def __init__(self):
        self.host = REDIS_CONFIG['default']['host']
        self.port = REDIS_CONFIG['default']['port']
        self.password = REDIS_CONFIG['default']['password']
        self.db = REDIS_CONFIG['default']['db']
        self.conn = redis.Redis(
            host=self.host,
            port=self.port,
            password=self.password,
            db=self.db
        )

    def set(self, name, value):
        a = self.conn.set(name=name, value=value, ex=CACHE_TIMEOUT)
        return a

    def get(self, name):
        value = self.conn.get(name=name)
        return value
