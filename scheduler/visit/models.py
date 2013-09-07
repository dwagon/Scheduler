import sys
import datetime

from django.db import models

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
def makeVisits(client, startDate, endDate):
    msgs=[]
    d=startDate
    d-=datetime.timedelta(days=1)
    sys.stderr.write("Making visists for %s\n" % client.name)
    lastvisit=None
    while d<endDate:
        d+=datetime.timedelta(days=1)
        day=Day.objects.get_or_create(date=d, defaults={'date':d})[0]
        if inGap(d):
            continue
        if day.isWeekend():
            continue
        if not client.goodDay(d):
            sys.stderr.write("%s is not a good day\n" % d)
            continue
        if day.canfit(client.duration):
            v=Visit(client=client, date=Day.objects.get(date=d))
            v.save()
            if lastvisit:
                delta=v.date-lastvisit.date
                desired=datetime.timedelta(days=7*client.regularity)
                if delta>desired:
                    msgs.append("Visit delta %s instead of %s (%s, last %s)\n" % (delta, desired, v.date, lastvisit.date))
                    v.good=False
                    v.save()
            lastvisit=v
            day.unfilled-=client.duration
            if day.unfilled:
                day.unfilled-=1 # Time to have lunch, travel, etc
            day.save()
            d+=datetime.timedelta(days=7*client.regularity)
            msgs.append("    Visit on %s\n" % day)
    return msgs

################################################################################
def clearVisits():
    for v in Visit.objects.all():
        v.delete()
    for d in Day.objects.all():
        d.delete()

#EOF
