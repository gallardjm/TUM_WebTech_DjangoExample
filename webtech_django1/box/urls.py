from django.conf.urls import patterns, url

from box import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.create, name='create'),
    url(r'^(?P<box_id>\d+)/$', views.read, name='read'),
    url(r'^update/(?P<box_id>\d+)/$', views.update, name='update'),
    url(r'^delete/$', views.delete, name='delete'),
)
