# -*- coding:utf-8 -*-
"""
    celery config
"""

from kombu import Queue, Exchange
import djcelery
import os
djcelery.setup_loader()

BROKER_BACKEND = 'redis'

BROKER_URL = 'redis://:'+os.getenv('REDIS_PASSWORD', 'syph@dev')+'@'+os.getenv('REDIS_HOST', 'redis_master')+':'+os.getenv('REDIS_PORT', '6379')+'/'+os.getenv('REDIS_DB_4_CELERY','2')

CELERY_TASK_SERIALIZER = 'json'

CELERYD_CONCURRENCY = 4
CELERYD_PREFETCH_MULTIPLIER = 8

CELERY_RESULT_BACKEND = 'djcelery.backends.database:DatabaseBackend'

# CELERY_IMPORTS = ("sreg_task", )

CELERY_QUEUES = (
    Queue('default',
          Exchange('default', type='direct'),
          routing_key='default'),
    Queue('re_task_audit',
          Exchange('re_task_audit', type='direct'),
          routing_key='re_task_audit'),
    Queue('re_task_store',
          Exchange('re_task_store', type='direct'),
          routing_key='re_task_store'),
)

CELERY_ROUTES = {
    'default': {'queue': 'default', 'routing_key': 'default'},
    'audit': {'queue': 're_task_audit', 'routing_key': 're_task_audit'},
    'store': {'queue': 're_task_store', 'routing_key': 're_task_store'},
}

CELERY_DEFAULT_QUEUE = 'default'
