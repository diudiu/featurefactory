#!/usr/bin/python

# -*- coding:utf-8 -*-
"""
    celery -A featurefactory worker -l debug --pool=solo
"""
import sys
import re
from celery.__main__ import main

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(main())