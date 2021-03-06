"""
Django settings for featurefactory project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0f6itw_sdz%*%0q7xqn2_y62-!3^)pj*o=m4cdloc@t#ey&oc^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'djcelery',
    # 'django.contrib.staticfiles',

    'apps.featureapi',
    'apps.common',
    'apps.datasource',
    'apps.remote',
    'apps.etl',
    'apps.async',
    'apps.pregranting',
    'apps.interface',
    'apps.integration',
    'apps.dispatcher'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'featurefactory.urls'

WSGI_APPLICATION = 'featurefactory.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
#
# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'collectstatic')
#
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, "static"),
# )

# MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
# MEDIA_URL = '/media/'
#
# TEMPLATE_DIRS = (os.path.join(BASE_DIR,  'templates'),)
#
# AUTH_USER_MODEL = ''
#
# LOGIN_URL = ''
# LOGIN_REDIRECT_URL = ''


from .dev_settings import *
# from .prod_settings import *
from celery_config import *
