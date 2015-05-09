# -*- coding: utf8 -*-
"""
Django settings for alpha project.

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
SECRET_KEY = '_3ofy%avg0dzb0j$2&ey4vfx&@kknfk)!s!m3!xpnrz1d+3=c4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    #'django.contrib.admin',
    #'django.contrib.auth',
    #'django.contrib.contenttypes',
    'django.contrib.sessions',
    #'django.contrib.messages',
    'django.contrib.staticfiles',
    'lnr',#login and regist注册登录app
    'blog',#此app涵盖了评测app页面的所有后端。
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    #'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    #'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    #'django.contrib.messages.middleware.MessageMiddleware',
    #'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'alpha.urls'

WSGI_APPLICATION = 'alpha.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

SYNCDB_LOCAL = True
#SYNCDB_LOCAL此变量作为同步到SAE和本地的开关。为True同步到SAE，为False同步到终端。
if 'SERVER_SOFTWARE' in os.environ:#此判断用于确定在SAE端和终端选择数据库的配置参数。
    from sae.const import (
        MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASS, MYSQL_DB
    )
else:
    if SYNCDB_LOCAL:
        MYSQL_HOST = 'w.rdc.sae.sina.com.cn'
        MYSQL_PORT = '3307'
        MYSQL_USER = '4ywmmyn0kz'
        MYSQL_PASS = 'y533w4xy5x4l0hlywlmy5zjijhwj3zjx5kw34imi'
        MYSQL_DB   = 'app_chanalpha'
        from sae._restful_mysql import monkey
        monkey.patch()
    else:
        MYSQL_HOST = 'localhost'
        MYSQL_PORT = '3306'
        MYSQL_USER = 'root'
        MYSQL_PASS = '123456'
        MYSQL_DB   = 'alpha'

DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.mysql',
        'NAME':     MYSQL_DB,
        'USER':     MYSQL_USER,
        'PASSWORD': MYSQL_PASS,
        'HOST':     MYSQL_HOST,
        'PORT':     MYSQL_PORT,
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

#TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False
#此处改为false在存入数据库的时候才不会导致时区变化，致使时间调整。


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

# 修改上传时文件在内存中可以存放的最大size为10m
FILE_UPLOAD_MAX_MEMORY_SIZE = 10485760
# sae的本地文件系统是只读的，修改django的file storage backend为Storage
DEFAULT_FILE_STORAGE = 'sae.ext.django.storage.backend.Storage'
# 使用media这个bucket
STORAGE_BUCKET_NAME = 'media'
# ref: https://docs.djangoproject.com/en/dev/topics/files/
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = '/media/'
#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
