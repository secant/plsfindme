from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.student import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'findme.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home, name='home'),
)
