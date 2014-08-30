from django.db import models

DOW_CHOICES = ((0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday'), (7, 'Anyday'))
DUR_CHOICES = ((0, 'Unknown'), (1, 'Hour'), (2, '1/4 Day'), (3, '1/3 Day'), (4, '1/2 Day'), (8, 'Full Day'))


################################################################################
################################################################################
################################################################################
class Client(models.Model):
    name = models.CharField(max_length=200, unique=True)
    regularity = models.IntegerField()
    dayofweek = models.SmallIntegerField(choices=DOW_CHOICES)
    duration = models.SmallIntegerField(choices=DUR_CHOICES)
    note = models.ForeignKey('Notes', null=True, blank=True)
    flexible = models.BooleanField(default=False)

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


################################################################################
################################################################################
################################################################################
class Gap(models.Model):
    start = models.DateField()
    end = models.DateField()

    ############################################################################
    def inGap(self, d):
        """ Is the date specified in the gap? """
        if d >= self.start and d <= self.end:
            return True
        return False


################################################################################
################################################################################
################################################################################
class Notes(models.Model):
    note = models.CharField(max_length=250)


################################################################################
def inGap(d):
    gaps = Gap.objects.all()
    for g in gaps:
        if d.inGap(d):
            return True
    return False

# EOF
