from base import *

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

DATABASES = {
    'default': {
    'ENGINE': 'sql_server.pyodbc',
    'NAME': 'APES_DJANGO',
    'USER': DB_USER,
    'PASSWORD': DB_PASS,
    'HOST': '10.0.0.133',
    'PORT': '1433',
     }
}

STATIC_URL = '/static/'
CRISPY_TEMPLATE_PACK  = 'bootstrap3'
#STATIC_ROOT =  os.path.join(BASE_DIR,'static') 

STATIC_PATH = os.path.join(BASE_DIR,'static')
              
STATICFILES_DIRS = ( os.path.join(BASE_DIR, "static1"), )
              
print "Static Path: %s " %STATIC_PATH
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
