from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns

from .views import generateAllVisits, VisitNew, VisitList, VisitDetail
from .views import VisitUpdate, VisitDelete, clearAllVisits
import restviews

api_patterns = [
    url(r'1/', include([
        url(r'^visit/$', restviews.VisitList.as_view()),
        url(r'^visit/(?P<pk>[0-9]+)/$', restviews.VisitDetail.as_view()),
        ])
    )
]

api_patterns = format_suffix_patterns(api_patterns)


urlpatterns = patterns('',
    url(r'^new/$', VisitNew.as_view(), name='visitNew'),
    url(r'^list/$', VisitList.as_view(), name='visitList'),
    url(r'^(?P<pk>\d+)/$', VisitDetail.as_view(), name='visitDetail'),
    url(r'^(?P<pk>\d+)/update$', VisitUpdate.as_view(), name='visitUpdate'),
    url(r'^(?P<pk>\d+)/delete$', VisitDelete.as_view(), name='visitDelete'),
    url(r'^generateVisits$', generateAllVisits, name='generateAllVisits'),
    url(r'^clearAllVisits$', clearAllVisits, name='clearAllVisits'),
    url(r'^api/', include(api_patterns)),
    )
