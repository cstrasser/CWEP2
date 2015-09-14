'''using nginx an gunicorn on our deploy server 10.0.0.111

website i used for original information:
http://michal.karzynski.pl/blog/2013/06/09/django-nginx-gunicorn-virtualenv-supervisor/'''


'''nginx  config file (not nginx.conf)
================================================================================='''
upstream django_server {
   server 127.0.0.1:8100; # i added this line as the one below(supplied did not work)
#   server unix:/webapps/django/run/gunicorn.sock fail_timeout=0;


upstream django_server {
   server 127.0.0.1:8100; # i added this line as the one below(supplied did not work)
#   server unix:/webapps/django/run/gunicorn.sock fail_timeout=0;
# to test gunicorn you can navigate to 10.0.0.111:8100 and if all ok you will see a page but no static files (formatting) 
 }

 server {

     listen   80;
     server_name django;
     client_max_body_size 4G;

     access_log /webapps/apesweb/logs/nginx-access.log;
     error_log /webapps/apesweb/logs/nginx-error.log ;
     # error_log /webapps/apesweb/logs/nginx-error.log debug ; #for debug level logging
 
     location /static/ {
         alias   /webapps/apesweb/static/;
     }

     location /media {
         alias  /webapps/apesweb/static/media;
     }
     location / {
         proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
         proxy_set_header Host $http_host;

       #   we don't want nginx trying to do something clever with
       #   redirects, we set the Host: header above already.
         proxy_redirect off;

        #  *application* server like Unicorn/Rainbows! serve static files.
         if (!-f $request_filename) {
             proxy_pass http://django_server;
             break;
         }
}
}
 
 '''#gunicorn_start.bash
============================================'''

#!/bin/bash

NAME="apesii"                                  # Name of the application
DJANGODIR=/webapps/apesweb                     # Django project directory
SOCKFILE=/webapps/apesweb/run/gunicorn.sock         # we will communicte using this unix socket
USER=ntwebuser                                 # the user to run as
GROUP=ntwebgroup                               # the group to run as
NUM_WORKERS=3                                  # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=apesii.settings.staging        # which settings file should Django use
#DJANGO_SETTINGS_MODULE = apesii.old_settings
DJANGO_WSGI_MODULE=apesii.wsgi                 # WSGI module name

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source bin/activate .

export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec /webapps/apesweb/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \  -b 0:8100
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=-
#=====================================================================================

''' other info:
# I added the below to wsgi.py when i had path problems, i am not sure if they are 100% required in
# the production wsgi but i lef them in because it was working
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))






