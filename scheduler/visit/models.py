import sys
import datetime

from django.db import models

from client.models import Client, Notes, inGap


################################################################################
################################################################################
################################################################################
class Visit(models.Model):
    client = models.ForeignKey(Client)
    good = models.BooleanField(default=True)
    date = models.DateField()
    note = models.ForeignKey(Notes, null=True, blank=True)

    def __str__(self):
        return "Visit %s on %s" % (self.client, self.date)

    class Meta:
        unique_together = (("client", "date"))


################################################################################
def newVisit(client, d):
    v = Visit(client=client, date=d)
    v.save()
    return v


################################################################################
def currentVisit(client, d):
    """ Return the visit if there is a current visit to this client on this day """
    visit = Visit.objects.filter(client=client, date=d)
    if visit:
        return visit[0]
    else:
        return None


################################################################################
def isWeekend(d):
    return d.weekday() in (5, 6)


################################################################################
def canFit(dt, dur):
    visits = Visit.objects.filter(date=dt)
    capacity = 8
    for v in visits:
        capacity -= v.client.duration
    return capacity >= dur


################################################################################
def makeVisits(client, startDate, endDate):
    msgs = []
    d = startDate
    d -= datetime.timedelta(days=1)
    clientRegularity = datetime.timedelta(days=7*client.regularity)
    sys.stderr.write("Making visists for %s (%s)\n" % (client.name, client.duration))
    lastdate = None
    while d < endDate:
        d += datetime.timedelta(days=1)
        if inGap(d):
            continue
        if isWeekend(d):
            continue
        if not client.goodDay(d):
            continue
        if lastdate:
            daysSince = d - lastdate
        else:
            daysSince = datetime.timedelta(days=9999999)
        if daysSince < clientRegularity:
            continue
        if canFit(d, client.duration):
            cv = currentVisit(client, d)
            if cv:
                lastdate = cv.date
                continue
            v = newVisit(client, d)
            if daysSince > clientRegularity:
                v.good = False
                v.save()
                msgs.append("Visit on %s - %s days since last once (meant to be %s days)" % (d, daysSince, clientRegularity))
            else:
                msgs.append("Visit on %s\n" % d)
            lastdate = v.date
    return msgs


################################################################################
def clearVisits():
    for v in Visit.objects.all():
        v.delete()

# EOF
