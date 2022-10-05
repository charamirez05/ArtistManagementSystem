from django.db import models

# Create your models here.

class Artist(models.Model):
    ArtistID = models.AutoField(primary_key=True)
    ArtistName = models.CharField(max_length=30)
    DebutDate = models.DateField()
    YearsActive = models.IntegerField(default=1)
    isActor = models.BooleanField(default=False)
    isSinger = models.BooleanField(default=False)
    Birthdate = models.DateField()


class Singer(Artist):
    Genre = models.CharField(max_length=50, null=False)
    FandomName = models.CharField(max_length=50, null=False)
    IsSolo = models.BooleanField(default=False)
    IsGroup = models.BooleanField(default=False)


class Singles(models.Model):
    singleID = models.AutoField(primary_key=True)
    singleName = models.CharField(max_length=30)
    recordedDate = models.DateField()
    releasedDate = models.DateField()
    genre = models.CharField(max_length=20)
    composer = models.CharField(max_length=30)
    producer = models.CharField(max_length=30)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE)


class Albums(models.Model):
    albumID = models.AutoField(primary_key=True)
    albumName = models.CharField(max_length=30)
    releasedDate = models.DateField()
    genre = models.CharField(max_length=30)
    dateRecorded = models.DateField()
    singles = models.ManyToManyField(Singles)
    Singer = models.ForeignKey(Singer, on_delete=models.CASCADE)


class Songs_Included(models.Model):
    albums = models.ForeignKey(Albums, on_delete=models.CASCADE)
    songsIncluded = models.CharField(max_length=50)

    class Meta:
        unique_together = ('albums', 'songsIncluded')