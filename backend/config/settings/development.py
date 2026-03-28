from .base import *
import os


DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "insurance",
        "USER": "postgres",
        "PASSWORD": "Pradip@7373",
        "HOST": "localhost",
        "PORT": "5432",
    }
}