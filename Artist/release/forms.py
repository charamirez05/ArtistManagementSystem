from django.forms import ModelForm
from django import forms

from .models import Artist, Albums, Singles


class SingerForm(ModelForm):
    Genre = forms.CharField(widget=forms.TextInput())
    FandomName = forms.CharField(widget=forms.TextInput())
    IsSolo = forms.CharField(widget=forms.CheckboxSelectMultiple())
    IsGroup = forms.CharField(widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Artist
        fields = ['Genre', 'FandomName', 'IsSolo', 'IsGroup']


class AlbumForm(ModelForm):
    AlbumName = forms.CharField(widget=forms.TextInput())
    ReleasedDate = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2023)))
    Genre = forms.CharField(widget=forms.TextInput())
    DateRecorded = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2023)))
    #SongIncluded

    class Meta:
        model = Albums
        fields = ['albumName', 'releasedDate', 'genre', 'dateRecorded']


class SinglesForm(ModelForm):
    singleName = forms.CharField(widget=forms.TextInput())
    recordedDate = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2023)))
    releasedDate = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2023)))
    genre = forms.CharField(widget=forms.TextInput())
    producer= forms.CharField(widget=forms.TextInput())
    composer = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = Singles
        fields = ['singleName', 'recordedDate', 'releasedDate', 'genre', 'producer', 'composer']