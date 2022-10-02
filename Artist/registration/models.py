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


class Actor(Artist):
    nationality = models.CharField(max_length=30)


class Films(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    films = models.CharField(max_length=50)

    class Meta:
        unique_together = ('actor', 'films')


class Specialization(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=50)

    class Meta:
        unique_together = ('actor', 'specialization')


class SoloArtist(Singer):
    StageName = models.CharField(max_length=30)


class Instruments(models.Model):
    soloArtist = models.ForeignKey(SoloArtist, on_delete=models.CASCADE)
    instruments = models.CharField(max_length=30)

    class Meta:
        unique_together = ('soloArtist', 'instruments')


class GroupArtist(Singer):
        dateFormed = models.DateField()


class GroupMembers(models.Model):
        GroupArtist = models.ForeignKey(GroupArtist, on_delete=models.CASCADE)
        GroupMembers = models.CharField(max_length=100)

        class Meta:
            unique_together = ('GroupArtist', 'GroupMembers')


class Singles(models.Model):
    SingleID = models.AutoField(primary_key=True)
    SingleName = models.CharField(max_length=30)
    RecordedDate = models.DateField()
    ReleasedDate = models.DateField()
    Genre = models.CharField(max_length=20)
    Composer = models.CharField(max_length=30)
    Producer = models.CharField(max_length=30)
    Singer = models.ForeignKey(Singer, on_delete=models.CASCADE)


class Albums(models.Model):
    albumID = models.AutoField(primary_key=True)
    albumName = models.CharField(max_length=30)
    releaseDate = models.DateField()
    genre = models.CharField(max_length=30)
    dateRecorded = models.DateField()
    singles = models.ManyToManyField(Singles)
    Singer = models.ForeignKey(Singer, on_delete=models.CASCADE)


class Songs_Included(models.Model):
    albums = models.ForeignKey(Albums, on_delete=models.CASCADE)
    songsIncluded = models.CharField(max_length=50)

    class Meta:
        unique_together = ('albums', 'songsIncluded')


class Platform(models.Model):
    platformName = models.CharField(max_length=30, primary_key=True)
    yearEstablished = models.BigIntegerField()
    ranking = models.IntegerField()
    singer = models.ManyToManyField(Singer)




