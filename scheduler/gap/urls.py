from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
import restviews

from .views import GapNew, GapList, GapDetail, GapUpdate, GapDelete, gapIndex

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
    url(r'^$', gapIndex, name='gapIndex'),
    url(r'^new/$', GapNew.as_view(), name='gapNew'),
    url(r'^list/$', GapList.as_view(), name='gapList'),
    url(r'^(?P<pk>\d+)/$', GapDetail.as_view(), name='gapDetail'),
    url(r'^(?P<pk>\d+)/update$', GapUpdate.as_view(), name='gapUpdate'),
    url(r'^(?P<pk>\d+)/delete$', GapDelete.as_view(), name='gapDelete'),
    url(r'^api/', include(api_patterns)),
)

# EOF
