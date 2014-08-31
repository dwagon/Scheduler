from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns

from .views import NoteDetail, NoteUpdate, NoteList, NoteDelete
from .views import NoteNew
import restviews

api_patterns = [
    url(r'1/', include([
        url(r'^notes/$', restviews.NoteList.as_view()),
        url(r'^notes/(?P<pk>[0-9]+)/$', restviews.NoteDetail.as_view()),
        ]
    ))
]

api_patterns = format_suffix_patterns(api_patterns)

urlpatterns = patterns(
    '',
    url(r'^new/$', NoteNew.as_view(), name='newNote'),
    url(r'^list/$', NoteList.as_view(), name='listNote'),
    url(r'^(?P<pk>\d+)/$', NoteDetail.as_view(), name='detailNote'),
    url(r'^(?P<pk>\d+)/update$', NoteUpdate.as_view(), name='updateNote'),
    url(r'^(?P<pk>\d+)/delete$', NoteDelete.as_view(), name='deleteNote'),
    url(r'^api/', include(api_patterns)),
    )

# EOF
