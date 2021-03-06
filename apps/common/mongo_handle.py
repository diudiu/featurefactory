# -*- coding:utf-8 -*-
"""
    mongo handler
"""
import logging
import pymongo
from django.utils.timezone import datetime
from featurefactory.settings import *

logger = logging.getLogger('apps.common')


def singleton(cls):
    instances = {}

    def _singleton(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return _singleton


class MongoBase(object):

    def __init__(self, collection_name):
        self.collection = collection_name
        host = MONGODB_HOST
        port = int(MONGODB_PORT)
        username = MONGODB_USERNAME
        password = MONGODB_PASSWORD
        db = MONGODB_NAME
        self.conn = pymongo.MongoClient(host=host, port=port)
        self.db = self.conn[db]
        if username and password:
            self.db.authenticate(username, password)
        self.coll = self.db[self.collection]

    def __del__(self):
        self.conn.close()

    def save(self, data):
        data.update({
            'create_time': datetime.now(),
            'update_time': datetime.now(),
        })
        return self.coll.insert_one(data)

    def update(self, key=None, query=None, data=None):
        if query is None:
            filte = {key: data[key]}
        else:
            filte = query
        if self.coll.find(filte).count() == 0:
            res = self.save(data)
        else:
            keys = data.keys()
            if '_id' in keys:
                del data['_id']
            res = self.coll.update_one(filte, {'$set': data})
        return res

    def search(self, query=None):
        if query is None:
            query = {}
        result = self.coll.find_one(query)
        return result
