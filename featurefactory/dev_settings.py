# -*- coding:utf-8 -*-

import os
import sys

DEBUG = True
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
PROJECT_PATH = os.path.dirname(CURRENT_PATH)


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'featuretemp',
        'NAME': 'featurefactory',
        'PASSWORD': '',
        'USER': 'root',
        'HOST': '192.168.1.196',
        'PORT': '8077',
    },
}
if 'test' in sys.argv:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'featuretemp',
        'NAME': 'featurefactory',
        'PASSWORD': '',
        'USER': 'root',
        'HOST': '192.168.1.196',
        'PORT': '8077',
        'TEST': {
            'CHARSET': 'utf8',
            'COLLATION': 'utf8_general_ci',
        },
    }

    TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# redis
REDIS_CONFIG = {
    'default': {
        'host': '192.168.1.198',
        'port': 6379,
        'password': 'syph@dev',
        'db': 7,
        'connect_timeout': 1,
    }
}


# mongodb
MONGODB_HOST = '192.168.1.198'
MONGODB_PORT = 27017
MONGODB_NAME = 'feature_storage'
MONGODB_USERNAME = 'feature_storage'
MONGODB_PASSWORD = 'feature_storage'

# logging
log_path = os.path.join(BASE_DIR, 'logs')
if not os.path.exists(log_path):
    os.makedirs(log_path)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[Level: %(levelname)s] %(asctime)s %(module)s %(process)d %(filename)s [line:%(lineno)d] '
                      '%(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'simple': {
            'format': '%(levelname)s %(asctime)s %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'handlers': {
        'common': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(log_path, 'apps.common.out'),
            'maxBytes': 1024 * 1024 * 20,
            'backupCount': 200,
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(log_path, 'apps.common.out'),
            'maxBytes': 1024 * 1024 * 20,
            'backupCount': 200,
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'featureapi': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(log_path, 'apps.common.out'),
            'maxBytes': 1024 * 1024 * 20,
            'backupCount': 200,
        },
        'datasource': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(log_path, 'apps.common.out'),
            'maxBytes': 1024 * 1024 * 20,
            'backupCount': 200,
        },
        'remote': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(log_path, 'apps.common.out'),
            'maxBytes': 1024 * 1024 * 20,
            'backupCount': 200,
        },
        'etl': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(log_path, 'apps.common.out'),
            'maxBytes': 1024 * 1024 * 20,
            'backupCount': 200,
        },
        'featuretest': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(log_path, 'apps.featuretest.out'),
            'maxBytes': 1024 * 1024 * 20,
            'backupCount': 200,
        },
        'pregranting': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(log_path, 'apps.pregranting.out'),
            'maxBytes': 1024 * 1024 * 20,
            'backupCount': 200,
        },
        'interface': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(log_path, 'apps.interface.out'),
            'maxBytes': 1024 * 1024 * 20,
            'backupCount': 200,
        },
        'integration': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(log_path, 'apps.integration.out'),
            'maxBytes': 1024 * 1024 * 20,
            'backupCount': 200,
        },
    },
    'loggers': {
        'django': {
            'handlers': ['common', 'console'],
            'level': 'INFO',
            'propagate': False,
        },
        'error': {
            'handlers': ['error', 'console'],
            'level': 'ERROR',
            'propagate': False,
        },
        'apps.featureapi': {
            'handlers': ['featureapi', 'console'],
            'level': 'INFO',
            'propagate': False,
        },
        'apps.common': {
            'handlers': ['common', 'console'],
            'level': 'INFO',
            'propagate': False,
        },
        'apps.datasource': {
            'handlers': ['datasource', 'console'],
            'level': 'INFO',
            'propagate': False,
        },
        'apps.remote': {
            'handlers': ['remote', 'console'],
            'level': 'INFO',
            'propagate': False,
        },
        'apps.etl': {
            'handlers': ['etl', 'console'],
            'level': 'INFO',
            'propagate': False,
        },
        'apps.featuretest': {
            'handlers': ['featuretest', 'console'],
            'level': 'INFO',
            'propagate': False,
        },
        'apps.pregranting': {
            'handlers': ['pregranting', 'console'],
            'level': 'INFO',
            'propagate': False,
        },
        'apps.interface': {
            'handlers': ['interface', 'console'],
            'level': 'INFO',
            'propagate': False,
        },
        'apps.integration': {
            'handlers': ['integration', 'console'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}
