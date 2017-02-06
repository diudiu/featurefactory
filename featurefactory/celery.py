# -*- coding:utf-8 -*-
"""
    django integrate celery.
    http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html

"""
from __future__ import absolute_import

import os  # noqa

from celery import Celery, platforms  # noqa

# set the default Django settings module for the 'celery' program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'featurefactory.settings')

from django.conf import settings  # noqa

import django  # noqa
from django.apps.registry import apps  # noqa
if django.VERSION >= (1, 7) and not apps.ready:
    pass

app = Celery('featurefactory')
platforms.C_FORCE_ROOT = True

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
    return 1234
