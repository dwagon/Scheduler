from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import login, logout
from django.conf import settings
from django.views.generic import RedirectView

from .views import index

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico')),
    url(r'^$', index, name='index'),
    url(r'^client/', include('client.urls')),
    url(r'^gap/', include('gap.urls')),
    url(r'^visit/', include('visit.urls')),
    url(r'^report/', include('report.urls')),

    url(r'^api/v1/gap/', include('gap.apiurls')),
    url(r'^api/v1/client/', include('client.apiurls')),
    url(r'^api/v1/visit/', include('visit.apiurls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/login/$',  login, {'template_name': 'base/login.html'}, name='login'),
    url(r'^accounts/logout/$', logout, {'next_page': '/'}, name='logout'),
)

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns(
        '',
        url(r'^__debug__/', include(debug_toolbar.urls)),
        )
