from django.conf.urls import patterns, url

from .views import ClientDetail, ClientUpdate, ClientList, ClientDelete
from .views import ClientNew, clientGenerateVisits, clientDeleteVisits
from .views import deleteAllClients, clientIndex

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
    url(r"^deleteAllClients$", deleteAllClients, name='deleteAllClients'),
    )

# EOF
