from django.db import models
from registration.models import Singer

# Create your models here.


class Concert (models.Model):
    ConcertName = models.CharField(max_length=100)
    VenueName = models.CharField(max_length=50)
    MaxParticipants = models.IntegerField()
    ConcertDate = models.DateField()
    Location = models.CharField(max_length=100)
    singer = models.ManyToManyField(Singer)
