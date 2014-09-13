from django.db import models

gaps = None


################################################################################
################################################################################
################################################################################
class Gap(models.Model):
    desc = models.CharField(max_length=250)
    start = models.DateField()
    end = models.DateField()

    class Meta:
        ordering = ['desc']

    ############################################################################
    def __str__(self):
        return "%s: %s to %s" % (self.desc, self.start, self.end)

    ############################################################################
    def inGap(self, d):
        """ Is the date specified in the gap? """
        if d >= self.start and d <= self.end:
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

# EOF
