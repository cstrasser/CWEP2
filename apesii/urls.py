"""apesii URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView


admin.site.site_header = 'APESII Administration'
#admin.site.register(Customer)
#admin.site.register(LocationMaster)
#admin.site.register(STO)
#admin.site.register(Contact)
from staff2.views import StaffUpdateView , StaffListView , StaffDetailView



urlpatterns = [
    #url(r'^sto/', include('sto.urls')),
    
    url(r'^login/$', include('logauth.urls')),
    url(r'^logout/$', 'logauth.views.user_logout', name='user_logout'),
    url(r'^about/$', 'logauth.views.about', name='about'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^staff/', include('staff.urls')),
    url(r'^navpage/$', 'navpage.views.navpage', name='navpage'),
    url(r'^sto/', include('sto.urls')),
    url(r'^$', RedirectView.as_view(url='/login', permanent=False), name='logindex'),
    url(r'^s1/(?P<pk>\d+)/$', view = StaffDetailView.as_view(), name = "staffdetailview"),
    url(r'^s2/(?P<pk>\d+)/$', view = StaffUpdateView.as_view(), name = "staffupdateview"),
    url(r'^s3', view = StaffListView.as_view(), name = "stafflistview"),
    
]
