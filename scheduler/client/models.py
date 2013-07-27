from django.db import models

DOW_CHOICES=((0,'Sunday'), (1,'Monday'), (2,'Tuesday'), (3,'Wednesday'), (4,'Thursday'), (5,'Friday'), (6,'Saturday'), (7,'Anyday'))
DUR_CHOICES=((0,'Unknown'), (1,'Hour'), (2,'1/4 Day'), (3,'1/3 Day'), (4, '1/2 Day'), (8,'Full Day'))

################################################################################
################################################################################
################################################################################
class Client(models.Model):
    name=models.CharField(max_length=200, unique=True)
    regularity=models.IntegerField()
    dayofweek=models.SmallIntegerField(choices=DOW_CHOICES)
    duration=models.SmallIntegerField(choices=DUR_CHOICES)
    note=models.ForeignKey('Notes', null=True, blank=True)

################################################################################
################################################################################
################################################################################
class Gap(models.Model):
    start=models.DateField()
    end=models.DateField()

################################################################################
################################################################################
################################################################################
class Visit(models.Model):
    client=models.ForeignKey(Client)
    date=models.DateField()
    note=models.ForeignKey('Notes')

################################################################################
################################################################################
################################################################################
class Notes(models.Model):
    note=models.CharField(max_length=250)

################################################################################
#EOF
