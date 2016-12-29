# -*- coding:utf-8 -*-

import abc
import json
import datetime
import logging

from bson.objectid import ObjectId

logger = logging.getLogger('apps.etl')


class BaseBackend(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def load(self):
        """ Load data from database """


class MongodbBackend(BaseBackend):
    def __init__(self, clazz, *args, **kwargs):
        self.clazz = clazz
        self.limit_start = kwargs.pop('limit_start', 0)
        self.limit_end = kwargs.pop('limit_end', 1)
        self.kwargs = kwargs
        super(MongodbBackend, self).__init__()

    def load(self, only_one=False, obj=False):
        """ Load data from Mongodb
            :param only_one, if True return objects[0],
            :param obj, if obj is True return document object else dict
        """
        objects = self.clazz.objects.filter(**self.kwargs)[self.limit_start:self.limit_end]
        if only_one and objects:
            if obj:
                objects = objects[0]
            else:
                objects = json.loads(objects[0].to_json())
                objects.pop("_id")
                for k, v in objects.iteritems():
                    if isinstance(v, dict):
                        if k == "_id":
                            objects.update({"_id": ObjectId(v["$oid"])})
                        elif v.get("$date"):
                            value = datetime.datetime.fromtimestamp(int(v["$date"]/1000))
                            objects.update({k: value})
                        elif isinstance(v.get("created_time"), dict):
                            v["created_time"] = datetime.datetime.fromtimestamp(int(v["created_time"]["$date"]/1000))

        return objects

    def save(self):
        """save document in Mongodb collection"""
        doc = self.clazz(**self.kwargs)

        logger.info("Mongodb model=%s, and save data=%s", self.clazz, self.kwargs)
        return doc.save()

    def update(self, query=None, **kwargs):
        """update value attribute for clazz
            :param, query, update for query documents
            :param, kwargs, key, value ready to update
        """
        if query is None:
            query = {}
        try:
            obj = self.clazz.objects.get(**query)
            obj.update(**kwargs)
            logger.info("Backend:%s update query:%s, data:%s", self.clazz, query, kwargs)
        except Exception as e:
            print e
            pass
