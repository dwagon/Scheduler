import sys
import datetime

from django.db import models

from client.models import Client, Notes, Day, inGap


################################################################################
################################################################################
################################################################################
class Visit(models.Model):
    client = models.ForeignKey(Client)
    good = models.BooleanField(default=True)
    date = models.ForeignKey(Day)
    note = models.ForeignKey(Notes, null=True, blank=True)

    def __str__(self):
        return "Visit %s on %s" % (self.client, self.date)

    class Meta:
        unique_together = (("client", "date"))


################################################################################
def newVisit(client, d):
    v = Visit(client=client, date=Day.objects.get(date=d))
    v.save()
    day = Day.objects.get_or_create(date=d, defaults={'date': d})[0]
    day.unfilled -= client.duration
    if day.unfilled:
        day.unfilled -= 1  # Time to have lunch, travel, etc
    day.save()
    return v


################################################################################
def makeVisits(client, startDate, endDate):
    msgs = []
    d = startDate
    d -= datetime.timedelta(days=1)
    sys.stderr.write("Making visists for %s (%s)\n" % (client.name, client.duration))
    lastdate = None
    while d < endDate:
        d += datetime.timedelta(days=1)
        day = Day.objects.get_or_create(date=d, defaults={'date': d})[0]
        if inGap(d):
            continue
        if day.isWeekend():
            continue
        if not client.goodDay(d):
            continue
        if lastdate and d-lastdate < datetime.timedelta(days=7*client.regularity):
            continue
        if day.canfit(client.duration):
            v = newVisit(client, d)
            if lastdate and d-lastdate > datetime.timedelta(days=7*client.regularity):
                v.good = False
                v.save()
                msgs.append("Visit on %s - %s days since last once (meant to be %s days)" % (day, d-lastdate, datetime.timedelta(days=7*client.regularity)))
            else:
                msgs.append("Visit on %s\n" % day)
            lastdate = v.date.date
    return msgs


################################################################################
def clearVisits():
    for v in Visit.objects.all():
        v.delete()
    for d in Day.objects.all():
        d.delete()

# EOF
