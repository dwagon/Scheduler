from django.db import models


################################################################################
################################################################################
################################################################################
class Gap(models.Model):
    desc = models.CharField(max_length=250)
    start = models.DateField()
    end = models.DateField()

    ############################################################################
    def inGap(self, d):
        """ Is the date specified in the gap? """
        if d >= self.start and d <= self.end:
            return True
        return False


################################################################################
def inGap(dt):
    gaps = Gap.objects.all()
    for gp in gaps:
        if gp.inGap(dt):
            return True
    return False

# EOF
