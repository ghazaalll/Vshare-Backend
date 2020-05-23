"""
Django settings for vshare project.
Generated by 'django-admin startproject' using Django 3.0.4.
For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
#this is features/online-users-backend
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@z)e)2eu^s1fk-9hfz)f66cf6--+dk1gle-hp((0q^nj!4u4^3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost','127.0.0.1']

# Application definition


INSTALLED_APPS = [
	'channels',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'groups.apps.GroupsConfig',
    'users',
    'stream',
	'corsheaders',
]

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer'
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser'
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    #'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    #'PAGE_SIZE': 3,
}

AUTH_USER_MODEL = 'users.Account'


MIDDLEWARE = [
	'corsheaders.middleware.CorsMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
    'corsheaders.middleware.CorsPostCsrfMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True


CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'Access-Control-Allow-Origin',
    'Access-Control-Allow-Headers',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'vshare.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'vshare.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'vshare',
        'USER' : 'admin',
        'PASSWORD' : 'vshare5432',
        'HOST' : 'localhost',
        'PORT' : '5432',
    }
}

redis_host = os.environ.get('REDIS_HOST', 'localhost')

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [(redis_host, 6379)],
        },
    }
}

ASGI_APPLICATION = 'vshare.routing.application'

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


REST_USE_JWT = True


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT = 'static'
# MEDIA_ROOT = 'media'

STATIC_URL = '/static/'
# MEDIA_URL = f"https://{AWS_S3_ENDPOINT_URL}/{MEDIA_ROOT}/"

# ########### django-storage ##############

# # Media files (Profile images, Videos)
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# # Static files (CSS, JavaScript, Images)
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# # Used to authenticate with S3
# AWS_ACCESS_KEY_ID = os.environ.get('S3_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = os.environ.get('S3_SECRET_ACCESS_KEY')

# Configure which endpoint to send files to, and retrieve files from.
# AWS_STORAGE_BUCKET_NAME = 'VshareBucket'
# AWS_S3_REGION_NAME = 'sfo2'
# AWS_S3_ENDPOINT_URL = f"https://{AWS_S3_REGION_NAME}.vshare.ir"
# AWS_S3_CUSTOM_DOMAIN =f"{AWS_STORAGE_BUCKET_NAME.{AWS_S3_REGION_NAME}.vshare.ir"
# AWS_LOCATION = 'files'

# # General optimization for faster delivery
# AWS_IS_GZIPPED = True
# AWS_S3_OBJECT_PARAMETERS = {
#     'CacheControl': 'max-age=86400',
# }

#permission