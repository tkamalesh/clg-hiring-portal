from django.conf.urls import include, url

from . import views

urlpatterns = [ 
    #url(r'^staff/',include('Academic.Staff.urls') ),
    url(r'^$', views.index, name='staffindex') ,
    url(r'^(?P<candidate_id>[0-9]+)/$', views.detail, name='staffdetail'),
    url(r'^(?P<candidate_id>[0-9]+)/forward/$', views.forward, name='stafforward'),
   url(r'^(?P<candidate_id>[0-9]+)/reject/$', views.reject, name='staffreject'),
    ]  
