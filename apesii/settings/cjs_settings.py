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
