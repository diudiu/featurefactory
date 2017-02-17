# -*- coding: utf-8 -*-

from apps.common.models import FeatureCodeMapping


class MysqlRepository(object):
    pass


class MongodbRepository(object):
    pass


class GenericRepository(MysqlRepository):
    pass


class FeatureRepository(MysqlRepository):

    model_cls = FeatureCodeMapping

    def find_all(self):
        query_sets = self.model_cls.objects.filter(is_delete=False)

        return query_sets
