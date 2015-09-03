from django.conf.urls import patterns, url
from sto import views

urlpatterns = (
    url(r'^$', 'sto.views.sto_list', name='sto_list'),
    url(r'filter/(?P<status>[\w\-]+)/$', 'sto.views.sto_list', name='sto_list'),
    url(r'testform/$', 'sto.views.sto_form', name='sto_form'),
    url(r'(?P<stid>\d+)/$', 'sto.views.sto_form', name ='sto_form'),
    
)