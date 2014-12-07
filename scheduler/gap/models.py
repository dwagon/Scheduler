from django.db import models

gaps = None


################################################################################
################################################################################
################################################################################
class Gap(models.Model):
    desc = models.CharField(max_length=250)
    start = models.DateField()
    end = models.DateField()
    recurring = models.BooleanField(default=True)

    class Meta:
        ordering = ['desc']

    ############################################################################
    def __str__(self):
        recur = ' (Recurring)' if self.recurring else ''
        return "%s: %s to %s%s" % (self.desc, self.start, self.end, recur)

    ############################################################################
    def inGap(self, d):
        """ Is the date specified in the gap? """
        if d >= self.start and d <= self.end:
            return True
        if self.recurring:
            year = d.year
            mod_start = self.start.replace(year=year)
            mod_end = self.end.replace(year=year)
            if d >= mod_start and d <= mod_end:
                return True
        return False


################################################################################
def inGap(dt):
    global gaps
    if not gaps:
        gaps = Gap.objects.all()
    for gp in gaps:
        if gp.inGap(dt):
            return gp
    return None


################################################################################
def clearGaps():
    for g in Gap.objects.all():
        g.delete()

# EOF
