from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

from findme.apps.student import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'findme.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name='home.html')),
]
