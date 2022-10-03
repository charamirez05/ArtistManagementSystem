from django.forms import ModelForm
from django import forms

from .models import Artist, Singer


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
    #films = forms.MultiValueField(widget=forms.MultiValueField())
   # specialization =forms.MultiValueField(widget=forms.MultiValueField())

    class Meta:
        model = Artist
        fields = ['nationality']


class SoloArtistForm(ModelForm):
    print()

class GroupArtistForm(ModelForm):
    print("WA GYUD GI EXTEND ANG CONTRACT SA IZ*ONE GRRR DISAPPOINTED KO >:<<")
