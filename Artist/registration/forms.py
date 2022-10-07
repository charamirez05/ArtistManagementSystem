from django.forms import ModelForm, MultiWidget
from django import forms

from .models import Artist, Singer, Actor



'''class ArtistForm(ModelForm):
    ArtistName = forms.CharField(widget=forms.TextInput())
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    # = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2023)))
    YearsActive = forms.CharField(widget=forms.NumberInput())
    isActor = forms.CheckboxSelectMultiple()
    isSinger = forms.CheckboxSelectMultiple()
   # Birthdate = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2023)))

    class Meta:
        model = Artist
        fields = ['ArtistName', 'username', 'password', 'YearsActive', 'isActor', 'isSinger']'''


class SingerForm(ModelForm):
    genreList = (('KP', 'KPop'), ('P', 'Pop'), ('HHR', 'Hip-Hop Rap'), ('C', 'Country'),
                 ('RB', 'Rhythm and Blues'), ('F', 'Folk'), ('J', 'Jazz'), ('HM', 'Heavy Metal'),
                 ('EDM', 'Electronic Dance Music'), ('S', 'Soul'), ('F', 'Funk'), ('R', 'Reggae'),
                 ('D', 'Disco'), ('PR', 'Punk Rock'), ('CL', 'Classical'), ('H', 'House'),
                 ('T', 'Techno'), ('IR', 'Indie Rock'), ('G', 'Grunge'), ('A', 'Ambient'),
                 ('R', 'Reggae'), ('S', 'Soul'), ('F', 'Funk'), ('R', 'Reggae'), ('G', 'Gospel'),
                 ('LM', 'Latin Music'), ('GM', 'Grime'), ('T', 'Trap'), ('PK', 'Psychedelic Rock'))
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    ArtistName = forms.CharField(widget=forms.TextInput())
    YearsActive = forms.CharField(widget=forms.NumberInput())
    Genre = forms.CharField(widget=forms.Select(choices=genreList))
    FandomName = forms.CharField(widget=forms.TextInput())
    isSinger = True
    IsSolo = forms.CheckboxSelectMultiple()
    IsGroup = forms.CheckboxSelectMultiple()

    class Meta:
        model = Singer
        fields = ['username', 'password', 'YearsActive', 'ArtistName', 'Genre', 'FandomName', 'IsSolo', 'IsGroup']


class ActorForm(ModelForm):
    specializationList = (('T', 'Theatre Acting'), ('TV', 'TV Acting'), ('F', 'Film Acting'), ('VO', 'Voice Over Acting'),
                          ('C', 'Commercials Acting'), ('EB', 'Extra/Background Acting'))
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    ArtistName = forms.CharField(widget=forms.TextInput())
    YearsActive = forms.CharField(widget=forms.NumberInput())
    specialization = forms.CharField(widget=forms.Select(choices=specializationList))
    nationality = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = Actor
        fields = ['username', 'password', 'YearsActive', 'ArtistName', 'nationality', 'specialization']


class SoloArtistForm(ModelForm):
    StageName = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = Artist
        fields = ['StageName']

    '''class Instruments(models.Model):
        soloArtist = models.ForeignKey(SoloArtist, on_delete=models.CASCADE)
        instruments = models.CharField(max_length=30)'''


class GroupArtistForm(ModelForm):
    dateFormed = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2023)))

    class Meta:
        model = Artist
        fields = ['dateFormed']

    '''class GroupMembers(models.Model):
        GroupArtist = models.ForeignKey(GroupArtist, on_delete=models.CASCADE)
        GroupMembers = models.CharField(max_length=100)

        class Meta:
            unique_together = ('GroupArtist', 'GroupMembers')'''
