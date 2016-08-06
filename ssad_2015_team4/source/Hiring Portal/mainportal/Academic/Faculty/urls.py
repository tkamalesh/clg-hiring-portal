from django.conf.urls import include, url

from . import views

urlpatterns = [ 
    url(r'^$', views.index, name='facultyindex') ,
    url(r'^(?P<candidate_id>[0-9]+)/$', views.detail, name='facultydetail'),
    url(r'^(?P<candidate_id>[0-9]+)/review/$', views.review, name='facultyreview'),
    ]  
