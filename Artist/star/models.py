from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.


class Artist(models.Model):
    username = models.CharField(max_length=15, null=False, primary_key=True)
    ArtistName = models.CharField(max_length=30, null=False)
    password = models.CharField(max_length=30, null=False)
    YearsActive = models.IntegerField(default=1, null=False)
    isActor = models.BooleanField(default=False)
    isSinger = models.BooleanField(default=False)
    Birthdate = models.DateField(null=False)
    DebutDate = models.DateField(null=False)


class Actor(Artist):
    specializationList = (('T', 'Theatre Acting'), ('TV', 'TV Acting'), ('F', 'Film Acting'), ('VO', 'Voice Over Acting'),
                        ('C', 'Commercials Acting'), ('EB', 'Extra/Background Acting'))
    nationality = models.CharField(max_length=30)
    specialization = MultiSelectField(choices=specializationList, max_length = 20)


class Film (models.Model):
    filmname = models.CharField(max_length=50)
    dateRelease = models.DateField()
    actorRole = models.CharField(max_length=30)
    director = models.CharField(max_length=30)
    actor = models.ManyToManyField(Actor)

