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

    def save(self, *args, **kwargs):
        if self.id:
            oldobj = Visit.objects.get(id=self.id)
            if oldobj.date != self.date:
                self.attn = True
                self.note += "[Moved from %s]" % oldobj.date
        super(Visit, self).save(*args, **kwargs)

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
    capacity = 8
    for v in visits:
        capacity -= v.client.duration
    return capacity >= dur


################################################################################
def makeVisits(client, startDate, endDate):
    msgs = []
    d = startDate - datetime.timedelta(days=1)
    # Find the first real start day
    for i in range(7 * client.regularity):
        d += datetime.timedelta(days=1)
        if client.goodDay(d) and canFit(d, client.duration):
            break
    else:
        # If we can't fit we may as well try and be on the right DoW
        d = startDate - datetime.timedelta(days=1)
        for i in range(7):
            d += datetime.timedelta(days=1)
            if client.goodDay(d):
                break

    clientRegularity = datetime.timedelta(days=7*client.regularity)
    while d < endDate:
        attn = False
        note = ''
        if inGap(d):
            attn = True
            note = "Originally on %s (%s)" % (d, inGap(d))
        if not canFit(d, client.duration):
            attn = True
            note = "Can't fit into %s" % d
        v = newVisit(client, d)
        v.attn = attn
        v.note = note
        v.save()
        d += clientRegularity

    return msgs


################################################################################
def clearVisits():
    for v in Visit.objects.all():
        v.delete()

# EOF
