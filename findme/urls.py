from django.conf.urls import patterns, include, url
from django.contrib import admin

from findme.apps.student import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'findme.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.form, name='home'),
    url(r'^form/$', views.form, name='form'),
    url(r'^submit/$', views.submit, name='submit'),
    url(r'^search/$', views.search, name='search'),
    url(r'^result/$', views.result, name='result'),
    url(r'^about/$', views.about, name='about'),
]