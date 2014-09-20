from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

import restviews

urlpatterns = [
    url(r'', include([
        url(r'^$', restviews.ClientList.as_view()),
        url(r'^(?P<pk>[0-9]+)/$', restviews.ClientDetail.as_view()),
        ]
    ))
]

urlpatterns = format_suffix_patterns(urlpatterns)

# EOF
