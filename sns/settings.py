"""
Django settings for sns project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from django.contrib.messages import constants as messages #追加
from django.contrib.messages import constants as message_constants #追加
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 'k*9t%-rev*(7+vxxky#t!%0z8k!%%!f)+5pn8wc+bcu5_ik0#o'



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#修正　'.herokuapp.app'　→ 'updatedsnsapp.herokuapp.com'
ALLOWED_HOSTS = ['127.0.0.1','.herokuapp.com','localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',
    'accounts',  # 追加
    'myposts', # 追加
    'bootstrap4', # 追加
    'imagekit',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sns.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
            'builtins': [
                'bootstrap4.templatetags.bootstrap4',
            ],
        },
    },
]

WSGI_APPLICATION = 'sns.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd9q41ted892o3k',
		'USER': 'ifxtmmivbvrllw',
		'PASSWORD': '96055db9950bd97676aa8d70d6e89fcfc986df6afcc59fd3a8d10475d90d47cb',
		'HOST': 'ec2-18-234-17-166.compute-1.amazonaws.com',
		'PORT': '5432',        
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
   os.path.join(BASE_DIR, "static"),
)
#パスワードのセキュリティーレベルをアップさせるためにBcryptを使用
PASSWORD_HASHERS = [
   'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
   'django.contrib.auth.hashers.BCryptPasswordHasher',
   'django.contrib.auth.hashers.PBKDF2PasswordHasher',
   'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
]

# 追加 mediaを扱うための設定
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIAFILES_DIRLS = (
    os.path.join(BASE_DIR,'media')
)

IMAGE_ROOT = os.path.join(BASE_DIR, 'images')
IMAGE_URL = '/images/','/avatar/'

# 追加 メッセージタグの設定
MESSAGE_TAGS = {
   messages.ERROR: 'alert alert-danger',
   messages.WARNING: 'alert alert-warning',
   messages.SUCCESS: 'alert alert-success',
   messages.INFO: 'alert alert-info'
}
AUTH_USER_MODEL = 'accounts.User'

LOGIN_URL = '/accounts/login'
LOGIN_REDIRECT_URL = '/accounts/userlist'
LOGOUT_REDIRECT_URL = '/accounts/login'

try:
	from .local_settings import *
except ImportError:
    pass

if not DEBUG:
	SECRET_KEY = os.environ['SECRET_KEY']
	import django_heroku
	django_heroku.settings(locals())

db_from_env = dj_database_url.config(conn_max_age=600, ssl_require=True)
DATABASES['default'].update(db_from_env)

# CLOUDINARY_STORAGE = {
#     'CLOUD_NAME'  : 'hy1khlpxs',
#     'API_KEY' : '576282828111838',
#     'API_SECRET' : 'zy7-b5Z9mAhR5z0Sb-2tm0oZ0OA',
# }

# DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'