from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import login, logout
from django.conf import settings

from .views import index, exportData


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', index, name='index'),
    url(r'^exportData$', exportData, name='exportData'),
    url(r'^client/', include('client.urls')),
    url(r'^gap/', include('gap.urls')),
    url(r'^visit/', include('visit.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$',  login, {'template_name': 'base/login.html'}, name='login'),
    url(r'^accounts/logout/$', logout, {'next_page': '/'}, name='logout'),
)

urlpatterns += staticfiles_urlpatterns()
