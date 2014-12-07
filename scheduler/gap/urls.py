from django.conf.urls import patterns, url

from .views import GapNew, GapList, GapDetail, GapUpdate, GapDelete
from .views import gapIndex, clearAllGaps

urlpatterns = patterns(
    '',
    url(r'^$', gapIndex, name='gapIndex'),
    url(r'^new/$', GapNew.as_view(), name='gapNew'),
    url(r'^list/$', GapList.as_view(), name='gapList'),
    url(r'^(?P<pk>\d+)/$', GapDetail.as_view(), name='gapDetail'),
    url(r'^(?P<pk>\d+)/update$', GapUpdate.as_view(), name='gapUpdate'),
    url(r'^(?P<pk>\d+)/delete$', GapDelete.as_view(), name='gapDelete'),
    url(r'^clearAllGaps$', clearAllGaps, name='clearAllGaps'),
)

# EOF
