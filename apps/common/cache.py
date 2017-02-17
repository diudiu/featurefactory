# -*- coding: utf-8 -*-

from apps.common.dao import FeatureRepository


class Singleton(type):
    def __init__(cls, name, bases, dicts):
        super(Singleton, cls).__init__(name, bases, dicts)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__call__(*args, **kwargs)

        return cls._instance


class FeatureGlobalCode(object):
    """
    特征的映射码值表，全局
    _feature_code_context data structure：
        {
            "education": [
                ("博士", 1),
                ("硕士", 2),
            ],
            "annual_income": [
                ([-1, 1000], 1),
                ([1000, 10000], 2),
            ],
        }

    :Usage 用法
        from apps.common.cache import feature_global_code

        feature_global_code.get("education")

    """
    __metaclass__ = Singleton

    _feature_code_context = None

    def __init__(self):
        self.feature_repository = FeatureRepository()

    def get(self, feature_name):
        if self._feature_code_context is None:
            self._load_data_from_db()

        if not isinstance(self._feature_code_context, dict):
            raise Exception("Feature code context is not initialize.")

        return self._feature_code_context.get(feature_name, None)

    def update(self):
        self._load_data_from_db()

    def _load_data_from_db(self):
        if self._feature_code_context is None:
            self.feature_repository.find_all()

feature_global_code = FeatureGlobalCode()

if __name__ == "__main__":
    o1 = FeatureGlobalCode()
    o2 = FeatureGlobalCode()

    print id(o1)
    print id(o2)
    assert o1 == o2