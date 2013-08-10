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
    note=models.ForeignKey('Notes', null=True, blank=True)

    class Meta:
        unique_together=(("client", "date"))

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

    def save(self):
        self.dayofweek=self.date.isoweekday()
        super(Day,self).save()

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
    sys.stderr.write("Making visists for %s\n" % client.name)
    while d<endDate:
        if inGap(d):
            continue
        if d.isoweekday()==client.dayofweek or client.dayofweek==7:
            day=Day.objects.get_or_create(date=d, defaults={'date':d})[0]
            v=Visit(client=client, date=Day.objects.get(date=d))
            v.save()
            d+=datetime.timedelta(days=7*client.regularity)
        else:
            d+=datetime.timedelta(days=1)

################################################################################
def initialiseDays(startDate, endDate):
    d=startDate
    while d<endDate:
        day=Day.objects.get_or_create(date=d, defaults={'date':d})[0]
        d+=datetime.timedelta(days=1)
#EOF
