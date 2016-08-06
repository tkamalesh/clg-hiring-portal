from django.conf.urls import url 

from . import views

urlpatterns = [ 
    url(r'^login$', views.login, name='facultylogin'),
    url(r'^logout/$', views.logout, name='facultylogout'),
    url(r'^callback$', views.callback, name='facultycallback'),
    ]
