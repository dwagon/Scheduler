from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns

from .views import ClientDetail, ClientUpdate, ClientList, ClientDelete
from .views import ClientNew, clientGenerateVisits, clientDeleteVisits
from .views import displayMonth, displayDay, displayClientMonth, clientIndex
import restviews

api_patterns = [
    url(r'1/', include([
        url(r'^client/$', restviews.ClientList.as_view()),
        url(r'^client/(?P<pk>[0-9]+)/$', restviews.ClientDetail.as_view()),
        ]
    ))
]

api_patterns = format_suffix_patterns(api_patterns)

urlpatterns = patterns(
    '',
    url(r'^$', clientIndex, name='clientIndex'),
    url(r'^new/$', ClientNew.as_view(), name='clientNew'),
    url(r'^list/$', ClientList.as_view(), name='clientList'),
    url(r'^(?P<pk>\d+)/$', ClientDetail.as_view(), name='clientDetail'),
    url(r'^(?P<pk>\d+)/update$', ClientUpdate.as_view(), name='clientUpdate'),
    url(r'^(?P<pk>\d+)/delete$', ClientDelete.as_view(), name='clientDelete'),
    url(r'^(?P<pk>\d+)/clientGenerateVisits$', clientGenerateVisits, name='clientGenerateVisits'),
    url(r'^(?P<pk>\d+)/clientDeleteVisits$', clientDeleteVisits, name='clientDeleteVisits'),
    url(r"^month/(\d+)/(\d+)/(prev|next)/$", displayMonth, name='displayYearMonthPage'),
    url(r"^month/(\d+)/(\d+)/$", displayMonth, name='displayYearMonth'),
    url(r"^month/(\d+)/$", displayMonth),
    url(r"^month/(?P<client>\d+)/$", displayClientMonth, name='displayClientMonth'),
    url(r"^month$", displayMonth, name='displayThisMonth'),
    url(r"^day/(\d+)/(\d+)/(\d+)/$", displayDay, name='displayDay'),
    url(r'^api/', include(api_patterns)),
    )

# EOF
