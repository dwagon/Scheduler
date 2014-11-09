import datetime

from django.db import models

from client.models import Client
from gap.models import inGap


################################################################################
################################################################################
################################################################################
class Visit(models.Model):
    client = models.ForeignKey(Client)
    attn = models.BooleanField("Attention Required", default=False)
    date = models.DateField()
    note = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return "Visit %s on %s" % (self.client, self.date)

    class Meta:
        unique_together = (("client", "date"))
        ordering = ['date']


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
    capacity = 9    # Hours in the day
    for v in visits:
        capacity -= v.client.duration
        # capacity -= 1   # Allow for travel
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
        # Skip weekends
        if d.isoweekday() in (6, 7):
            continue
        if not client.goodDay(d):
            continue
        daysSince = d - lastdate
        if daysSince < clientRegularity:
            continue
        if canFit(d, client.duration):
            v = newVisit(client, d)
            if inGap(d):
                v.attn = True
                v.note = "Originally on %s (%s)" % (d, inGap(d))
                v.save()
            if firstVisit:
                firstVisit = False
            elif daysSince > clientRegularity:
                v.attn = True
                v.save()
                msgs.append("Visit on %s - %s days since last (meant to be %s days)" % (d, daysSince.days, clientRegularity.days))
            lastdate = v.date
            continue

    return msgs


################################################################################
def clearVisits():
    for v in Visit.objects.all():
        v.delete()

# EOF
