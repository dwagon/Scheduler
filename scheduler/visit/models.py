import datetime

from django.db import models

from client.models import Client
from gap.models import inGap


################################################################################
################################################################################
################################################################################
class Visit(models.Model):
    client = models.ForeignKey(Client)
    good = models.BooleanField(default=True)
    date = models.DateField()
    note = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return "Visit %s on %s" % (self.client, self.date)

    class Meta:
        unique_together = (("client", "date"))


################################################################################
def newVisit(client, d):
    v = currentVisit(client, d)
    if not v:
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
        capacity -= 1   # Allow for travel
    return capacity >= dur


################################################################################
def makeVisits(client, startDate, endDate):
    msgs = []
    d = startDate
    d -= datetime.timedelta(days=1)
    clientRegularity = datetime.timedelta(days=7*client.regularity)
    lastdate = datetime.date(year=1990, month=1, day=1)
    firstVisit = True
    while d < endDate:
        d += datetime.timedelta(days=1)
        if not tryDay(client, d):
            continue
        if not client.goodDay(d):
            continue
        daysSince = d - lastdate
        if daysSince < clientRegularity:
            continue
        if canFit(d, client.duration):
            v = newVisit(client, d)
            if firstVisit:
                firstVisit = False
            elif daysSince > clientRegularity and not client.flexible:
                v.good = False
                v.save()
                msgs.append("Visit on %s - %s days since last (meant to be %s days)" % (d, daysSince.days, clientRegularity.days))
            lastdate = v.date
            continue

        if client.flexible:
            v = createFlexibleVisit(client, d)
            if v:
                lastdate = v.date

    return msgs


################################################################################
def createFlexibleVisit(client, d):
    for delta in (1, 2):
        for sign in (-1, 1):
            newdate = d + datetime.timedelta(days=sign*delta)
            if not tryDay(client, newdate):
                continue
            if canFit(newdate, client.duration):
                v = newVisit(client, newdate)
                return v
    return None


################################################################################
def tryDay(client, d):
    if inGap(d):
        return False
    if isWeekend(d):
        return False
    return True


################################################################################
def clearVisits():
    for v in Visit.objects.all():
        v.delete()

# EOF
