from django.db import models
# Create your models here.


class Artist(models.Model):
    #ArtistID = models.AutoField(primary_key=True)
    ArtistName = models.CharField(max_length=30)
    username = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=30)
    #DebutDate = models.DateField(null=False)
    YearsActive = models.IntegerField(default=1)
    isActor = models.BooleanField(default=False)
    isSinger = models.BooleanField(default=False) #mo redirect sa lain html
    #Birthdate = models.DateField(null=False)


class Actor(Artist):
    specializationList = (('T', 'Theatre Acting'), ('TV', 'TV Acting'), ('F', 'Film Acting'), ('VO', 'Voice Over Acting'),
                 ('C', 'Commercials Acting'), ('EB', 'Extra/Background Acting'))
    nationality = models.CharField(max_length=30)
    specialization = models.CharField(max_length=3, choices=specializationList)


class Film (models.Model):
    filmname = models.CharField(max_length=50)
    dateRelease = models.DateField()
    actorRole = models.CharField(max_length=30)
    director = models.CharField(max_length=30)
    actor = models.ManyToManyField(Actor)

