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
        'NAME': 'featurefactory',
        'PASSWORD': '123456',    # 123456
        'USER': 'dev',   # riskcontrol_dev
        'HOST': '192.168.1.198',   # 192.168.0.198
        'PORT': '3306'  # 3306
    },
}
if 'test' in sys.argv:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'featurefactory',
        'PASSWORD': '123456',
        'USER': 'root',
        'HOST': '192.168.1.198',
        'PORT': '3306',
        'TEST': {
            'CHARSET': 'utf8',
            'COLLATION': 'utf8_general_ci'
        }
    }

    TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# redis
REDIS_CONFIG = {
    'default': {
        'host': '192.168.1.198',
        'port': 6379,
        'password': 'syph@dev',
        'db': 0,
        'connect_timeout': 1
    }
}

# mongodb
MONGODB_CONFIG = {
    'default': {
        'host': '192.168.1.198',
        'port': 27017,
        'username': '',
        'password': '',
        'db': 'featurefactory',
        'connect': False
    }
}

# logging
log_path = os.path.join(BASE_DIR, 'logs')
if not os.path.exists(log_path):
    os.makedirs(log_path)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(filename)s [line:%(lineno)d] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(asctime)s %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    'handlers': {
        'common': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(log_path, 'apps.common.out'),
            'maxBytes': 1024 * 1024 * 20,
            'backupCount': 200
        },
        'error': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(log_path, 'apps.error.out'),
            'maxBytes': 1024 * 1024 * 20,
            'backupCount': 200
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'featureapi': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(log_path, 'apps.featureapi.out'),
            'maxBytes': 1024 * 1024 * 20,
            'backupCount': 200
        },
    },
    'loggers': {
        'django': {
            'handlers': ['common', 'console'],
            'level': 'INFO',
            'propagate': False
        },
        'apps.featureapi': {
            'handlers': ['common', 'console'],
            'level': 'INFO',
            'propagate': False
        },
    }
}
