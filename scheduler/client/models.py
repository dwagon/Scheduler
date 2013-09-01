from django.db import models
import sys
import datetime

DOW_CHOICES=((0,'Monday'), (1,'Tuesday'), (2,'Wednesday'), (3,'Thursday'), (4,'Friday'), (5,'Saturday'), (6,'Sunday'), (7,'Anyday'))
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
    def __str__(self):
        return "%s" % self.name

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
class Notes(models.Model):
    note=models.CharField(max_length=250)

################################################################################
################################################################################
################################################################################
class Day(models.Model):
    date=models.DateField(unique=True)
    dayofweek=models.SmallIntegerField(choices=DOW_CHOICES)
    unfilled=models.SmallIntegerField(default=8)

    def save(self, *args, **kwargs):
        self.dayofweek=self.date.isoweekday()
        super(Day,self).save(*args, **kwargs)

    def __str__(self):
        return "%s" % self.date

################################################################################
def inGap(d):
    gaps=Gap.objects.all()
    for g in gaps:
        if d.inGap(d):
            return True
    return False

################################################################################
def initialiseDays(startDate, endDate):
    d=startDate
    while d<endDate:
        day=Day.objects.get_or_create(date=d, defaults={'date':d})[0]
        d+=datetime.timedelta(days=1)

#EOF
