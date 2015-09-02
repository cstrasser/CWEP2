from base import *

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
#STATIC_ROOT =  "C:\users\cstrasser\documents\git_repo\apesii\apesii\"
STATIC_ROOT = "c:\
"
#os.path.join(BASE_DIR, "static)
print "static root:%s " %STATIC_ROOT
STATIC_PATH = os.path.join(BASE_DIR,'static')
#STATIC_PATH = "C:\users\cstrasser\documents\git_repo\\apesii\\apesii\
              
STATICFILES_DIRS = ( os.path.join(BASE_DIR, "static"), )
              
print "Static Path: %s " %STATIC_PATH
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
