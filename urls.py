from django.conf.urls import patterns, url

from grabdatax import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^goto/$', views.goto, name='goto'),
    url(r'^list/$', views.list, name='list'),
)
