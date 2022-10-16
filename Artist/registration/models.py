from django.db import models
from multiselectfield import MultiSelectField


# Create your models here.


class Artist(models.Model):
    username = models.CharField(max_length=15, null=False, primary_key=True)
    ArtistName = models.CharField(max_length=30, null=False)
    password = models.CharField(max_length=30, null=False)
    YearsActive = models.IntegerField(default=1, null=False)
    isActor = models.BooleanField(default=0)
    isSinger = models.BooleanField(default=0)


class Singer(Artist):
    genreList = (('KP', 'KPop'), ('P', 'Pop'), ('HHR', 'Hip-Hop Rap'), ('C', 'Country'),
                 ('RB', 'Rhythm and Blues'), ('F', 'Folk'), ('J', 'Jazz'), ('HM', 'Heavy Metal'),
                 ('EDM', 'Electronic Dance Music'), ('S', 'Soul'), ('F', 'Funk'), ('R', 'Reggae'),
                 ('D', 'Disco'), ('PR', 'Punk Rock'), ('CL', 'Classical'), ('H', 'House'),
                 ('T', 'Techno'), ('IR', 'Indie Rock'), ('G', 'Grunge'), ('A', 'Ambient'),
                 ('R', 'Reggae'), ('S', 'Soul'), ('F', 'Funk'), ('R', 'Reggae'), ('G', 'Gospel'),
                 ('LM', 'Latin Music'), ('GM', 'Grime'), ('T', 'Trap'), ('PK', 'Psychedelic Rock'))

    instrumentList = (('AG', 'Acoustic Guitar'), ('BJ', 'Banjo'), ('B', 'Bass'), ('CL', 'Cello'), ('C', 'Clarinet'),
                       ('EG', 'Electric Guitar'), ('D', 'Drums'), ('F', 'Flute'), ('PKO', 'Piano/Keyboard/Organ'),
                      ('S', 'Saxophone'),  ('T', 'Trumpet'),  ('U', 'Ukelele'), ('V', 'Voice only'), ('V', 'Violin'))

    Genre = MultiSelectField(max_length=30, choices=genreList)
    Instruments = MultiSelectField(choices=instrumentList, max_length=20)
    FandomName = models.CharField(max_length=50, null=False)


class Actor(Artist):
    specializationList = (('T', 'Theatre Acting'), ('TV', 'TV Acting'), ('F', 'Film Acting'), ('VO', 'Voice Over Acting'),
                        ('C', 'Commercials Acting'), ('EB', 'Extra/Background Acting'))
    nationality = models.CharField(max_length=30)
    specialization = MultiSelectField(choices=specializationList, max_length = 20)






