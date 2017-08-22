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
from vendor.utils import constant as cons

CACHE_TIMEOUT = cons.CACHE_TIMEOUT


def singleton(cls):
    instances = {}

    def _singleton(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return _singleton


@singleton
class RedisX(object):
    def __init__(self):
        self.host = REDIS_CONFIG['default']['host']
        self.port = int(REDIS_CONFIG['default']['port'])
        self.password = REDIS_CONFIG['default']['password']
        self.db = int(REDIS_CONFIG['default']['db'])
        self.conn = redis.Redis(
            host=self.host,
            port=self.port,
            password=self.password,
            db=self.db
        )

    def ping(self):
        try:
            self.conn.ping()
        except:
            self.conn = redis.Redis(
                host=self.host,
                port=self.port,
                password=self.password,
                db=self.db
            )

    def delete(self, key):
        a = self.conn.delete(key)
        return a

    def set(self, name, value):
        self.ping()
        a = self.conn.set(name=name, value=value, ex=CACHE_TIMEOUT)
        return a

    def get(self, name):
        self.ping()
        value = self.conn.get(name=name)
        return value

    def sadd(self, name, value):
        a = self.conn.sadd(name, value)
        return a

    def srem(self, name, value):
        a = self.conn.srem(name, value)
        return a

    def smembers(self, name):
        a = self.conn.smembers(name=name)
        return a

    def rpush(self, name, value):
        a = self.conn.rpush(name, value)
        return a

    def llen(self, name):
        a = self.conn.llen(name)
        return a

    def lrem(self, name, value, num=1):
        a = self.conn.lrem(name=name, value=value, num=num)
        return a

    def incr(self, name, amount=1):
        a = self.conn.incr(name, amount)
        return a

    def decr(self, name, amount=1):
        a = self.conn.decr(name, amount)
        return a

    def expire(self, name, time=CACHE_TIMEOUT):
        a = self.conn.expire(name, time)
        return a
