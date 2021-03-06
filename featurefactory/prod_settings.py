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
        'NAME': os.getenv('MYSQL_DATABASE', 'featurefactory'),
        'PASSWORD': os.getenv('MYSQL_PASSWORD', '123456'),
        'USER': os.getenv('MYSQL_USER', 'dev'),
        'HOST': os.getenv('MYSQL_HOST', 'mysql_master'),
        'PORT': os.getenv('MYSQL_PORT', '3306'),
    },
}
if 'test' in sys.argv:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('MYSQL_DATABASE', 'featurefactory'),
        'PASSWORD': os.getenv('MYSQL_USER', '123456'),
        'USER': os.getenv('MYSQL_USER', 'dev'),
        'HOST': os.getenv('MYSQL_HOST', 'mysql_master'),
        'PORT': os.getenv('MYSQL_PORT', '3306'),
        'TEST': {
            'CHARSET': 'utf8',
            'COLLATION': 'utf8_general_ci',
        },
    }
    TEST_RUNNER = 'django.test.runner.DiscoverRunner'
# redis
REDIS_CONFIG = {
    'default': {
        'host': os.getenv('REDIS_HOST', 'redis_master'),
        'port': int(os.getenv('REDIS_PORT', '6379')),
        'password': os.getenv('REDIS_PASSWORD', 'syph@dev'),
        'db': int(os.getenv('REDIS_DB_4_FF', '1')),
        'connect_timeout': 1,
    }
}
# mongodb
MONGODB_HOST = os.getenv('MONGODB_HOST', 'mongodb_primary')
MONGODB_PORT = int(os.getenv('MONGODB_PORT', '27017'))
MONGODB_NAME = os.getenv('MONGODB_DATABASE', 'feature_storage')
MONGODB_USERNAME = os.getenv('MONGODB_USERNAME', 'feature_storage')
MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD', 'feature_storage')

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
            'maxBytes': 1024 * 1024 * 100,
            'backupCount': 5,
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(log_path, 'apps.common.out'),
            'maxBytes': 1024 * 1024 * 100,
            'backupCount': 5,
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
            'maxBytes': 1024 * 1024 * 100,
            'backupCount': 5,
        },
        'datasource': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(log_path, 'apps.common.out'),
            'maxBytes': 1024 * 1024 * 100,
            'backupCount': 5,
        },
        'remote': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(log_path, 'apps.common.out'),
            'maxBytes': 1024 * 1024 * 100,
            'backupCount': 5,
        },
        'etl': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(log_path, 'apps.common.out'),
            'maxBytes': 1024 * 1024 * 100,
            'backupCount': 5,
        },
        'featuretest': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(log_path, 'apps.common.out'),
            'maxBytes': 1024 * 1024 * 100,
            'backupCount': 5,
        },
        'pregranting': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(log_path, 'apps.common.out'),
            'maxBytes': 1024 * 1024 * 100,
            'backupCount': 5,
        },
        'interface': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(log_path, 'apps.common.out'),
            'maxBytes': 1024 * 1024 * 100,
            'backupCount': 5,
        },
        'integration': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(log_path, 'apps.common.out'),
            'maxBytes': 1024 * 1024 * 100,
            'backupCount': 5,
        },
        'dispatcher': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(log_path, 'apps.dispatcher.out'),
            'maxBytes': 1024 * 1024 * 100,
            'backupCount': 5,
        },
        'timelog': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(log_path, 'apps.timelog.out'),
            'maxBytes': 1024 * 1024 * 100,
            'backupCount': 5,
        }
    },
    'loggers': {
        'django': {
            'handlers': ['common'],
            'level': 'INFO',
            'propagate': False,
        },
        'error': {
            'handlers': ['error'],
            'level': 'ERROR',
            'propagate': False,
        },
        'apps.featureapi': {
            'handlers': ['featureapi'],
            'level': 'INFO',
            'propagate': False,
        },
        'apps.common': {
            'handlers': ['common'],
            'level': 'INFO',
            'propagate': False,
        },
        'apps.datasource': {
            'handlers': ['datasource'],
            'level': 'INFO',
            'propagate': False,
        },
        'apps.remote': {
            'handlers': ['remote'],
            'level': 'INFO',
            'propagate': False,
        },
        'apps.etl': {
            'handlers': ['etl'],
            'level': 'INFO',
            'propagate': False,
        },
        'apps.featuretest': {
            'handlers': ['featuretest'],
            'level': 'INFO',
            'propagate': False,
        },
        'apps.pregranting': {
            'handlers': ['pregranting'],
            'level': 'INFO',
            'propagate': False,
        },
        'apps.interface': {
            'handlers': ['interface'],
            'level': 'INFO',
            'propagate': False,
        },
        'apps.integration': {
            'handlers': ['integration'],
            'level': 'INFO',
            'propagate': False,
        },
        'apps.dispatcher': {
            'handlers': ['dispatcher'],
            'level': 'INFO',
            'propagate': False,
        },
        'apps.timelog': {
            'handlers': ['timelog'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}
