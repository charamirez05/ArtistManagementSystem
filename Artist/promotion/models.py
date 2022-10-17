
from django.db import models
from registration.models import Singer

# Create your models here.


class Platform(models.Model):
    platformName = models.CharField(max_length=30)
    yearEstablished = models.CharField(max_length=4)
    ranking = models.IntegerField()
    singer = models.ManyToManyField(Singer)