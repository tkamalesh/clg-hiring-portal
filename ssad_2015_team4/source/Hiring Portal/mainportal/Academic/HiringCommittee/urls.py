from django.conf.urls import include, url

from . import views

urlpatterns = [ 
    url(r'^$', views.index, name='hiringcomindex') ,
    url(r'^(?P<candidate_id>[0-9]+)/$', views.detail, name='hiringcomdetail'),
    url(r'^(?P<candidate_id>[0-9]+)/forward/$', views.forward, name='hiringcomforward'),
    url(r'^(?P<candidate_id>[0-9]+)/addfaculty/$', views.addfaculty, name='hiringfacultyadd'),
    url(r'^(?P<candidate_id>[0-9]+)/review/$', views.review, name='hiringcomreview'),
    url(r'^(?P<candidate_id>[0-9]+)/reject/$', views.reject, name='hiringcomreject'),
    url(r'^(?P<candidate_id>[0-9]+)/interview/$', views.interview, name='hiringcominterview'),
    ]  
