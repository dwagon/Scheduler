from django.conf.urls import patterns, url

from .views import ClientDetail, ClientUpdate, ClientList, ClientDelete
from .views import ClientNew, index, generateVisits, generateAllVisits
from .views import displayMonth, displayDay, clearAllVisits

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^new/$', ClientNew.as_view(), name='newClient'),
    url(r'^list/$', ClientList.as_view(), name='listClients'),
    url(r'^(?P<pk>\d+)/$', ClientDetail.as_view(), name='detailClient'),
    url(r'^(?P<pk>\d+)/update$', ClientUpdate.as_view(), name='updateClient'),
    url(r'^(?P<pk>\d+)/delete$', ClientDelete.as_view(), name='clientDelete'),
    url(r'^(?P<pk>\d+)/generateVisits$', generateVisits, name='generateVisits'),
    url(r'^generateVisits$', generateAllVisits, name='generateAllVisits'),
    url(r'^clearAllVisits$', clearAllVisits, name='clearAllVisits'),
    url(r"^month/(\d+)/(\d+)/(prev|next)/$", displayMonth, name='displayYearMonthPage'),
    url(r"^month/(\d+)/(\d+)/$", displayMonth, name='displayYearMonth'),
    url(r"^month/(\d+)/$", displayMonth),
    url(r"^month$", displayMonth, name='displayThisMonth'),
    url(r"^day/(\d+)/(\d+)/(\d+)/$", displayDay, name='displayDay'),
    )
