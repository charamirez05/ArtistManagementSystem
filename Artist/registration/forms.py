from django.forms import ModelForm, MultiWidget
from django import forms

from .models import Artist, Singer, Actor


#Hello uyst welcome to my vlog
class ArtistForm(ModelForm):
    ArtistName = forms.CharField(widget=forms.TextInput())
    DebutDate = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2023)))
    YearsActive = forms.CharField(widget=forms.NumberInput())
    isActor = forms.CheckboxSelectMultiple()
    isSinger = forms.CheckboxSelectMultiple()
    Birthdate = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2023)))

    class Meta:
        model = Artist
        fields = ['ArtistName', 'DebutDate', 'YearsActive', 'isActor', 'isSinger', 'Birthdate']


class SingerForm(ModelForm):
    Genre = forms.CharField(widget=forms.TextInput())
    FandomName = forms.CharField(widget=forms.TextInput())
    IsSolo = forms.CharField(widget=forms.CheckboxSelectMultiple())
    IsGroup = forms.CharField(widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Singer
        fields = ['Genre', 'FandomName', 'IsSolo', 'IsGroup']


class ActorForm(ModelForm):
    nationality = forms.CharField(widget=forms.TextInput())
   # films = forms.CharField(widget=forms.TextInput())
   # specialization =forms.MultiValueField(widget=forms.MultiValueField())

    class Meta:
        model = Actor
        fields = ['nationality']

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
