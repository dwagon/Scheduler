from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from .views import index

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^client/', include('client.urls')),
    url(r'^visit/', include('visit.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
