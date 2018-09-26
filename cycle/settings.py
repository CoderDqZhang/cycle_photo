"""
Django settings for cycle project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-+c*dm%gor8eoalqqzs-=o0xt$)&iqmbzbbeeunh0@hi2qk5-0'


#七牛云存储
QINIU_ACCESS_KEY = 'lGDN5XTYH4HWk_i7GRre-izRRk3AE7gmxL5u6I0t'
QINIU_SECRET_KEY = 'vpryXIs8kIJ3pWUfGmK1Y4vnHhOCRO5xMDQwN50m'
QINIU_BUCKET_NAME = 'ball'
QINIU_BUCKET_DOMAIN = 'p9it92m77.bkt.clouddn.com'
QINIU_SECURE_URL = True      #使用http

#七牛保存图片
MEDIA_URL1 = "http://"+QINIU_BUCKET_DOMAIN + "/"
MEDIA_ROOT1 = os.path.join(BASE_DIR, 'media')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

STATIC_URL = '/static/'

STATIC_PATH = os.path.join( os.path.dirname(__file__) , 'static' )

#本地保存图片
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# Application definition

INSTALLED_APPS = [
    #'xadmin',
    #'crispy_forms',
    'reversion',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'photo'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cycle.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'cycle.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'photo',
        'USER': 'root',
        'PASSWORD': 'root123',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_TZ = False

USE_I18N = True

USE_L10N = True


DEFAULT_FILE_STORAGE = 'qiniustorage.backends.QiniuStorage'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
HERE = os.path.dirname(os.path.dirname(__file__))

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(HERE, "../cycle/photo/static/").replace('\\', '/')
