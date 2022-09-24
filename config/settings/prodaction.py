from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'todo',
        'USER': 'yamamotod',
        'PASSWORD': '88888888',
        'HOST': 'db',
        'PORT': '5432',
    }
}