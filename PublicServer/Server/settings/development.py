
from .base import *

DEBUG = True

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

