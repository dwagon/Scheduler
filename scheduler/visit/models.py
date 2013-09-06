from django.db import models
import sys
import datetime
from client.models import Client, Notes, Day, inGap

################################################################################
################################################################################
################################################################################
class Visit(models.Model):
    client=models.ForeignKey(Client)
    good=models.BooleanField(default=True)
    date=models.ForeignKey(Day)
    note=models.ForeignKey(Notes, null=True, blank=True)

    def __str__(self):
        return "Visit %s on %s" % (self.client, self.date)

    class Meta:
        unique_together=(("client", "date"))

################################################################################
def inWeekend(day):
    if day.weekday() in (5,6):
        return True
    return False

################################################################################
def makeVisits(client, startDate, endDate):
    d=startDate
    d-=datetime.timedelta(days=1)
    sys.stderr.write("Making visists for %s\n" % client.name)
    while d<endDate:
        d+=datetime.timedelta(days=1)
        if inGap(d):
            continue
        if inWeekend(d):
            continue
        if d.weekday()==client.dayofweek or client.dayofweek==7:
            day=Day.objects.get_or_create(date=d, defaults={'date':d})[0]
            if day.unfilled>=client.duration:
                v=Visit(client=client, date=Day.objects.get(date=d))
                v.save()
                day.unfilled-=client.duration
                if day.unfilled:
                    day.unfilled-=1 # Time to have lunch, travel, etc
                day.save()
                d+=datetime.timedelta(days=7*client.regularity)
                sys.stderr.write("    Visit on %s\n" % day)
                continue
            else:
                d+=datetime.timedelta(days=7)

################################################################################
def clearVisits():
    for v in Visit.objects.all():
        v.delete()
    for d in Day.objects.all():
        d.delete()

#EOF
