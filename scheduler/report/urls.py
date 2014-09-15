from django.conf.urls import patterns, url
from .reports import reportIndex, displayMonth, displayYear
from .reports import displayDay, exportData

urlpatterns = patterns(
    '',
    url(r'^$', reportIndex, name='reportIndex'),
    url(r"^month/(\d+)/(\d+)/(prev|next)/$", displayMonth, name='displayYearMonthPage'),
    url(r"^month/(\d+)/(\d+)/$", displayMonth, name='displayYearMonth'),
    url(r"^month/(\d+)/$", displayMonth),
    url(r"^month$", displayMonth, name='displayThisMonth'),
    url(r"^year/$", displayYear, name='displayYear'),
    url(r"^year/(\d+)$", displayYear, name='displayYear'),
    url(r"^day/(\d+)/(\d+)/(\d+)/$", displayDay, name='displayDay'),
    url(r'^exportData$', exportData, name='exportData'),
    )

# EOF
