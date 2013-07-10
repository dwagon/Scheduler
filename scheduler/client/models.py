from django.db import models

DOW_CHOICES=((0,'Sunday'), (1,'Monday'), (2,'Tuesday'), (3,'Wednesday'), (4,'Thursday'), (5,'Friday'), (6,'Saturday'))

class Client(models.Model):
    name=models.CharField(max_length=200)
    regularity=models.IntegerField()
    dayofweek=models.SmallIntegerField(choices=DOW_CHOICES)
    note=models.ForeignKey('Notes')

class Gap(models.Model):
    start=models.DateField()
    end=models.DateField()

class Visit(models.Model):
    client=models.ForeignKey(Client)
    date=models.DateField()
    note=models.ForeignKey('Notes')

class Notes(models.Model):
    note=models.CharField(max_length=250)

#EOF
