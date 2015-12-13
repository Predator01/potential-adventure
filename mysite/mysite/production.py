from common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'twitter2',
        'USER': 'twitter2',
        'PASSWORD': 'twitter2',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
