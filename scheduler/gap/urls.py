from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
import restviews

from .views import GapNew, GapList, GapDetail, GapUpdate, GapDelete

api_patterns = [
    url(r'1/', include([
        url(r'^gap/$', restviews.GapList.as_view()),
        url(r'^gap/(?P<pk>[0-9]+)/$', restviews.GapDetail.as_view()),
        ]
    ))
]

api_patterns = format_suffix_patterns(api_patterns)

urlpatterns = patterns(
    '',
    url(r'^new/$', GapNew.as_view(), name='newGap'),
    url(r'^list/$', GapList.as_view(), name='listGap'),
    url(r'^(?P<pk>\d+)/$', GapDetail.as_view(), name='detailGap'),
    url(r'^(?P<pk>\d+)/update$', GapUpdate.as_view(), name='updateGap'),
    url(r'^(?P<pk>\d+)/delete$', GapDelete.as_view(), name='deleteGap'),
    url(r'^api/', include(api_patterns)),
)

# EOF
