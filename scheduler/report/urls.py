from django.conf.urls import patterns, url
from .reports import reportIndex, displayMonth, displayYear
from .reports import displayDay, exportData, clientReport

urlpatterns = patterns(
    '',
    url(r'^$', reportIndex, name='reportIndex'),
    url(r"^month/(\d+)/(\d+)/$", displayMonth, name='displayYearMonth'),
    url(r"^month/(\d+)/$", displayMonth),
    url(r"^month$", displayMonth, name='displayThisMonth'),
    url(r"^year/$", displayYear, name='displayYear'),
    url(r"^year/(?P<year>\d+)$", displayYear, name='displayYear'),
    url(r"^day/(\d+)/(\d+)/(\d+)/$", displayDay, name='displayDay'),
    url(r'^exportData$', exportData, name='exportData'),
    url(r'^client$', clientReport, name='clientReport'),
    )

# EOF
