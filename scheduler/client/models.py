from django.db import models
from note.models import Note

DOW_CHOICES = (
    (0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'),
    (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday'), (7, 'Anyday'))

DUR_CHOICES = (
    (0, 'Unknown'), (1, 'Hour'), (2, '1/4 Day'), (3, '1/3 Day'),
    (4, '1/2 Day'), (8, 'Full Day'))


################################################################################
################################################################################
################################################################################
class Client(models.Model):
    name = models.CharField(max_length=200, unique=True)
    regularity = models.PositiveSmallIntegerField(help_text="How many weeks between visits")
    dayofweek = models.SmallIntegerField(choices=DOW_CHOICES)
    duration = models.SmallIntegerField(choices=DUR_CHOICES)
    note = models.ForeignKey(Note, null=True, blank=True)
    flexible = models.BooleanField(default=False, help_text="Try adjacent days to fit in visit")
    startdate = models.DateField(null=True, default=None, help_text="Schedule visits from this date")
    enddate = models.DateField(null=True, default=None, help_text="Schedule visits until this date")

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

# EOF
