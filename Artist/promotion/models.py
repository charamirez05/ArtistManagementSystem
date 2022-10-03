from django.db import models

# Create your models here.

class Artist(models.Model):
    ArtistID = models.AutoField(primary_key=True)
    ArtistName = models.CharField(max_length=30)
    DebutDate = models.DateField()
    YearsActive = models.IntegerField(default=1)
    isActor = models.BooleanField(default=False)
    isSinger = models.BooleanField(default=False) #mo redirect sa lain html
    Birthdate = models.DateField()

class Singer(Artist):
    Genre = models.CharField(max_length=50, null=False)
    FandomName = models.CharField(max_length=50, null=False)
    IsSolo = models.BooleanField(default=False)
    IsGroup = models.BooleanField(default=False)

class Platform(models.Model):
    platformName = models.CharField(max_length=30, primary_key=True)
    yearEstablished = models.BigIntegerField()
    ranking = models.IntegerField()
    singer = models.ManyToManyField(Singer)
