# -*- coding:utf-8 -*-
"""
    feature api models
"""
from django.db import models

from apps.common.models import BaseModel


class ClientOverview(BaseModel):
    """
        client_code and other messages
    """
    client_code = models.CharField(u'', max_length=128)
    client_id = models.CharField(u'', max_length=128)
    client_secret = models.CharField(u'', max_length=256)
    des_key = models.CharField(u'', max_length=128)
    manage_type = models.CharField(u'', max_length=256)

    class Meta:
        db_table = 'fic_client_overview'
        verbose_name = u''
        verbose_name_plural = u''
