from django.conf.urls import patterns, url

from .views import generateAllVisits, VisitNew, VisitList, VisitDetail
from .views import VisitUpdate, VisitDelete, clearAllVisits


urlpatterns = patterns(
    '',
    url(r'^new/(?P<clientid>\d+)$', VisitNew.as_view(), name='visitNew'),
    url(r'^list/$', VisitList.as_view(), name='visitList'),
    url(r'^(?P<pk>\d+)/$', VisitDetail.as_view(), name='visitDetail'),
    url(r'^(?P<pk>\d+)/update$', VisitUpdate.as_view(), name='visitUpdate'),
    url(r'^(?P<pk>\d+)/delete$', VisitDelete.as_view(), name='visitDelete'),
    url(r'^generateVisits$', generateAllVisits, name='generateAllVisits'),
    url(r'^clearAllVisits$', clearAllVisits, name='clearAllVisits'),
    )
