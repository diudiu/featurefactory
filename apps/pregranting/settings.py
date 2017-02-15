# -*- coding: utf-8 -*-

import logging
from django.utils.importlib import import_module

logger = logging.getLogger('apps.openapi')

PRE_GRANT_MODEL_CLS = 'apps.pregranting.sublevel.LinearPreGrant'


def get_pre_grant_model(identity):
    try:
        package_str = PRE_GRANT_MODEL_CLS[:PRE_GRANT_MODEL_CLS.rindex('.')]
        class_str = PRE_GRANT_MODEL_CLS[PRE_GRANT_MODEL_CLS.rindex('.') + 1:]
        package = import_module(package_str)
        model_cls = getattr(package, class_str, None)
        if model_cls is not None:
            return model_cls(identity)

        raise ImportError('Can not import class of %s' % PRE_GRANT_MODEL_CLS)
    except (ImportError, TypeError) as e:
        logger.error(e.message, exc_info=True)
