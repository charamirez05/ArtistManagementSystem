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



class Singer(Artist):
    genreList = (('KP', 'KPop'), ('P', 'Pop'), ('HHR', 'Hip-Hop Rap'), ('C', 'Country'),
                 ('RB', 'Rhythm and Blues'), ('F', 'Folk'), ('J', 'Jazz'), ('HM', 'Heavy Metal'),
                 ('EDM', 'Electronic Dance Music'), ('S', 'Soul'), ('F', 'Funk'), ('R', 'Reggae'),
                 ('D', 'Disco'), ('PR', 'Punk Rock'), ('CL', 'Classical'), ('H', 'House'),
                 ('T', 'Techno'), ('IR', 'Indie Rock'), ('G', 'Grunge'), ('A', 'Ambient'),
                 ('R', 'Reggae'), ('S', 'Soul'), ('F', 'Funk'), ('R', 'Reggae'), ('G', 'Gospel'),
                 ('LM', 'Latin Music'), ('GM', 'Grime'), ('T', 'Trap'), ('PK', 'Psychedelic Rock'))
    Genre = models.CharField(max_length=3, choices=genreList)
    FandomName = models.CharField(max_length=50, null=False)
    IsSolo = models.BooleanField(default=False)
    IsGroup = models.BooleanField(default=False)


class Actor(Artist):
    specializationList = (('T', 'Theatre Acting'), ('TV', 'TV Acting'), ('F', 'Film Acting'), ('VO', 'Voice Over Acting'),
                 ('C', 'Commercials Acting'), ('EB', 'Extra/Background Acting'))
    nationality = models.CharField(max_length=30)
    specialization = models.CharField(max_length=3, choices=specializationList)


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


class Platform(models.Model):
    platformName = models.CharField(max_length=30, primary_key=True)
    yearEstablished = models.BigIntegerField()
    ranking = models.IntegerField()
    singer = models.ManyToManyField(Singer)




