
from . import base

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'raspi_db',
        'USER': 'django',
        'PASSWORD': 'djangoraspipostgre',
        'HOST': 'localhost',
        'PORT': '',
    }
}