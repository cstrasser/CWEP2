"""
Django settings for apesii project.
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from keys import DB_PASS, DB_USER, DJANGO_SECRET_KEY
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print "BASE DIR:%s " %BASE_DIR
SECRET_KEY = 'DJANGO_SECRET_KEY'

DEBUG = True
ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms', 
    'logauth',
    'staff',
    'navpage',
    'staff2',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'apesii.urls'

TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')
print "Template PAth:%s " %TEMPLATE_PATH
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_PATH],
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

WSGI_APPLICATION = 'apesii.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
    'ENGINE': 'sql_server.pyodbc',
    'NAME': 'APES_DJANGO',
    'USER': DB_USER,
    'PASSWORD': DB_PASS,
    'HOST': '10.0.0.133',
    'PORT': '1433',
    'OPTIONS': {
      'host_is_server': True,
      'dsn': 'ntdsrc',
      'driver' : 'FreeTDS',
      'extra_params' : 'TDS_VERSION=8.0'
     }
   }
}


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
CRISPY_TEMPLATE_PACK  = 'bootstrap3'
STATIC_ROOT =  os.path.join(BASE_DIR, "static")
STATIC_PATH = os.path.join(BASE_DIR,'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


