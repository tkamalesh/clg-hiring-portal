from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login$', views.login, name='candidatelogin'),
    url(r'^register$', views.register, name='candidateregister'),
    url(r'^logout/$', views.logout, name='candidatelogout'),
    url(r'^register_success/$', views.register_success, name='register_success'),
    url(r'^confirm/(?P<activation_key>\w+)/', views.register_confirm, name='register_confirm'),
    ]
