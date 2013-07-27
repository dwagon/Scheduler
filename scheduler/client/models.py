from django.db import models
import sys
import datetime

DOW_CHOICES=((0,'Sunday'), (1,'Monday'), (2,'Tuesday'), (3,'Wednesday'), (4,'Thursday'), (5,'Friday'), (6,'Saturday'), (7,'Anyday'))
DUR_CHOICES=((0,'Unknown'), (1,'Hour'), (2,'1/4 Day'), (3,'1/3 Day'), (4, '1/2 Day'), (8,'Full Day'))

################################################################################
################################################################################
################################################################################
class Client(models.Model):
    name=models.CharField(max_length=200, unique=True)
    regularity=models.IntegerField()
    dayofweek=models.SmallIntegerField(choices=DOW_CHOICES)
    duration=models.SmallIntegerField(choices=DUR_CHOICES)
    note=models.ForeignKey('Notes', null=True, blank=True)

    ############################################################################
    def populateVisits(self):
        pass

################################################################################
################################################################################
################################################################################
class Gap(models.Model):
    start=models.DateField()
    end=models.DateField()

    ############################################################################
    def inGap(self, d):
        """ Is the date specified in the gap? """
        if d>=self.start and d<=self.end:
            return True
        return False

################################################################################
################################################################################
################################################################################
class Visit(models.Model):
    client=models.ForeignKey(Client)
    date=models.ForeignKey('Day')
    note=models.ForeignKey('Notes')

################################################################################
################################################################################
################################################################################
class Notes(models.Model):
    note=models.CharField(max_length=250)

################################################################################
################################################################################
################################################################################
class Day(models.Model):
    date=models.DateField(unique=True)
    dayofweek=models.SmallIntegerField(choices=DOW_CHOICES)
    unfilled=models.SmallIntegerField()

################################################################################
def inGap(d):
    gaps=Gap.objects.all()
    for g in gaps:
        if d.inGap(d):
            return True
    return False

################################################################################
def makeVisits(client, startDate, endDate):
    d=startDate
    while d<endDate:
        if inGap(d):
            continue
        # TODO - make this bit
        d+=datetime.timedelta(days=1)

################################################################################
def initialiseDays(startDate, endDate):
    d=startDate
    while d<endDate:
        try:
            day=Day.objects.get(date=d)
        except Day.DoesNotExist:
            day=Day(date=d, dayofweek=d.isoweekday(), unfilled=8)
            day.save()
        else:
        d+=datetime.timedelta(days=1)
#EOF
