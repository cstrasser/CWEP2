from django.conf.urls import patterns, url
from . import views

urlpatterns = (
    
    url(r'^$', 'logauth.views.ntlogin', name='ntlogin'),
    url(r'^logout/$', views.user_logout, name='logout'),
     
    # url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    # url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    # url(r'^accounts/loggedin/$', 'views.success', name='success'),
    # 
    
    
    
)



# url(r'filter/(?P<status>[\w\-]+)/$', 'sto.views.sto_list', name='sto_list'),
#     #url(r'^category/(?P<category_name_url>[\w\-]+)/$', views.category, name='category'),
#     url(r'testform/$', 'sto.views.sto_form', name='sto_form'),
#     url(r'(?P<stid>\d+)/$', 'sto.views.sto_form', name ='sto_form'),
#     #url(r'about/$', 'main.views.about', name='about'),


# urlpatterns = patterns('',
#         url(r'^$', views.index, name='index'),
#         url(r'about/', views.about, name='about'),
#         url(r'^add_category/$', views.add_category, name='add_category'),
#         url(r'^add_page/(?P<category_name_slug>[\w\-]+)/$', views.add_page, name='add_page'),
#         url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
#         url(r'^goto/(?P<page_id>\d+)/$', views.track_URL, name ='goto'),
#         
#         url(r'^restricted/', views.restricted, name='restricted'),
#         #url(r'^register/$', views.register, name='register'), # removed due to implemetation of registration redux
#         #url(r'^login/$', views.user_login, name='login'), # removed due to implemetation of registration redux 
#         #url(r'^logout/$', views.user_logout, name ='logout')
# )  
#         