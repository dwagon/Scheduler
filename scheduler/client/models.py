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
class Visit(models.Model):
    client=models.ForeignKey(Client)
    good=models.BooleanField(default=True)
    date=models.ForeignKey('Day')
    note=models.ForeignKey('Notes', null=True, blank=True)

    def __str__(self):
        return "Visit %s on %s" % (self.client, self.date)

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

    def save(self, *args, **kwargs):
        self.dayofweek=self.date.weekday()
        super(Day,self).save(*args, **kwargs)

    def __str__(self):
        return "%s" % self.date

################################################################################
def isWeekend(d):
    if d.weekday() in (5,6):
        return True
    return False

################################################################################
def inGap(d):
    gaps=Gap.objects.all()
    for g in gaps:
        if d.inGap(d):
            return True
    return False

################################################################################
def makeVisits(client, startDate, endDate):
    d=startDate-datetime.timedelta(days=1)
    sys.stderr.write("Calculating for %s\n" % client.name)
    while d<endDate:
        d+=datetime.timedelta(days=1)
        if inGap(d):
            continue
        if isWeekend(d):
            continue
        if d.weekday()==client.dayofweek or client.dayofweek==7:
            day=Day.objects.get_or_create(date=d, defaults={'date':d})[0]
            if day.unfilled>=client.duration:
                v=Visit(client=client, date=Day.objects.get(date=d))
                v.save()
                day.unfilled-=client.duration
                if day.unfilled:
                    day.unfilled-=1 # Time to have lunch, travel etc
                day.save()
                d+=datetime.timedelta(days=7*client.regularity)
                continue
            else:
                v=Visit(client=client, date=Day.objects.get(date=d), good=False)
                v.save()

################################################################################
def clearVisits():
    for v in Visit.objects.all():
        v.delete()
    for d in Day.objects.all():
        d.delete()

################################################################################
def initialiseDays(startDate, endDate):
    d=startDate
    while d<endDate:
        day=Day.objects.get_or_create(date=d, defaults={'date':d})[0]
        d+=datetime.timedelta(days=1)
#EOF
