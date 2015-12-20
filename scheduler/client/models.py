from django.db import models
import datetime

DOW_CHOICES = (
    (0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'),
    (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday'), (7, 'Anyday'))


################################################################################
################################################################################
################################################################################
class Client(models.Model):
    name = models.CharField(max_length=200, unique=True)
    regularity = models.PositiveSmallIntegerField(help_text="How many weeks between visits")
    dayofweek = models.SmallIntegerField(choices=DOW_CHOICES)
    duration = models.SmallIntegerField(default=0, help_text="Number of hours per visit")
    note = models.CharField(max_length=250, blank=True)
    flexible = models.BooleanField(default=False)   # Legacy
    startdate = models.DateField(null=True, default=None, help_text="Schedule visits from this date (YYYY-MM-DD)")
    enddate = models.DateField(null=True, default=None, help_text="Schedule visits until this date (YYYY-MM-DD)")

    class Meta:
        ordering = ['name']

    ############################################################################
    def daterange(self):
        if not self.startdate and not self.enddate:
            return ""
        outstr = ""
        if self.startdate:
            outstr += "%s -" % self.startdate
        if self.enddate:
            outstr += " %s" % self.enddate
        else:
            outstr += " onwards"
        return outstr

    ############################################################################
    def __str__(self):
        return "%s" % self.name

    ############################################################################
    def goodDay(self, d):
        if self.dayofweek == 7:
            return True
        if d.weekday() == self.dayofweek:
            return True
        return False

    ############################################################################
    def makeVisits(self, startdate=None, enddate=None):
        from visit.models import makeVisits
        today = datetime.datetime.now()
        if self.startdate:
            start = self.startdate
        else:
            start = datetime.date(today.year, 1, 1)
        if self.enddate:
            end = self.enddate
        else:
            end = datetime.date(today.year+1, 12, 31)
        if self.regularity != 0:
            msgs = makeVisits(self, start, end)
        else:
            msgs = []
        return msgs

# EOF
