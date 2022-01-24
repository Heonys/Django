from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0&4(%&o+--&n1ry748aak855t+6177(ho70^9c1c58)o3vz=pk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'pass1234',
        'HOST': 'mariadb',
        'PORT': '3306',
    }
}