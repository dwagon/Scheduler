from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns

from .views import ClientDetail, ClientUpdate, ClientList, ClientDelete
from .views import ClientNew, index, generateVisits
from .views import displayMonth, displayDay, displayClientMonth
import restviews

api_patterns = [
    url(r'1/', include([
        url(r'^client/$', restviews.ClientList.as_view()),
        url(r'^client/(?P<pk>[0-9]+)/$', restviews.ClientDetail.as_view()),
        url(r'^gap/$', restviews.GapList.as_view()),
        url(r'^gap/(?P<pk>[0-9]+)/$', restviews.GapDetail.as_view()),
        url(r'^notes/$', restviews.NotesList.as_view()),
        url(r'^notes/(?P<pk>[0-9]+)/$', restviews.NotesDetail.as_view()),
        ]
    ))
]

api_patterns = format_suffix_patterns(api_patterns)

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^new/$', ClientNew.as_view(), name='newClient'),
    url(r'^list/$', ClientList.as_view(), name='listClients'),
    url(r'^(?P<pk>\d+)/$', ClientDetail.as_view(), name='detailClient'),
    url(r'^(?P<pk>\d+)/update$', ClientUpdate.as_view(), name='updateClient'),
    url(r'^(?P<pk>\d+)/delete$', ClientDelete.as_view(), name='clientDelete'),
    url(r'^(?P<pk>\d+)/generateVisits$', generateVisits, name='generateVisits'),
    url(r"^month/(\d+)/(\d+)/(prev|next)/$", displayMonth, name='displayYearMonthPage'),
    url(r"^month/(\d+)/(\d+)/$", displayMonth, name='displayYearMonth'),
    url(r"^month/(\d+)/$", displayMonth),
    url(r"^month/(?P<client>\d+)/$", displayClientMonth, name='displayClientMonth'),
    url(r"^month$", displayMonth, name='displayThisMonth'),
    url(r"^day/(\d+)/(\d+)/(\d+)/$", displayDay, name='displayDay'),
    url(r'^api/', include(api_patterns)),
    )
