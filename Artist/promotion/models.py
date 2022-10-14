from django.db import models

from registration.models import Singer


# Create your models here.


class Platform(models.Model):
    platformName = models.CharField(max_length=30, primary_key=True)
    yearEstablished = models.BigIntegerField()
    ranking = models.IntegerField()
    singer = models.ManyToManyField(Singer, related_name='platformsinger')
