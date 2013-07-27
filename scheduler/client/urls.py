from django.conf.urls import patterns, url

from .views import ClientDetail, ClientUpdate, ClientList, ClientDelete
from .views import ClientNew, index, viewCalendar, generateVisits

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^new/$', ClientNew.as_view(), name='newClient'),
    url(r'^list/$', ClientList.as_view(), name='listClients'),
    url(r'^(?P<pk>\d+)/$', ClientDetail.as_view(), name='detailClient'),
    url(r'^(?P<pk>\d+)/update$', ClientUpdate.as_view(), name='updateClient'),
    url(r'^(?P<pk>\d+)/delete$', ClientDelete.as_view(), name='clientDelete'),
    url(r'^viewCalendar$', viewCalendar, name='viewCalendar'),
    url(r'^generateVisits$', generateVisits, name='generateVisits'),
    )
