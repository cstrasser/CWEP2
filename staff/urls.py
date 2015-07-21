
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
        
    # url(r'^login/', include('logauth.urls')),
    # url(r'^logout/', 'logauth.views.logout', name='logout'),
    # url(r'^about/$', 'logauth.views.about', name='about'),
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'staff.views.stafflist', name = 'stafflist'),
    url(r'^(?P<staff_id>\d+)/$', 'staff.views.staffform', name ='staffform'),
    
]
