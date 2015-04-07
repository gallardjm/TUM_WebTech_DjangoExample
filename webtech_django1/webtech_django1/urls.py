from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    #Admin site
    url(r'^admin/', include(admin.site.urls)),
    
    #Box app
    url(r'^box/', include('box.urls', namespace='box')),
    
    #user login/logout
    url('^login/','django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url('^logout/','django.contrib.auth.views.logout', {'template_name': 'logout.html'}, name='logout'),
)
