from django.forms import ModelForm
from django import forms

from .models import Album, Single



class AlbumForm(ModelForm):
    AlbumName = forms.CharField(widget=forms.TextInput())
    ReleasedDate = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2023)))
    Genre = forms.CharField(widget=forms.TextInput())
    DateRecorded = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2023)))

    class Meta:
        model = Album
        fields = ['albumName', 'releasedDate', 'genre', 'dateRecorded']


class SinglesForm(ModelForm):
    singleName = forms.CharField(widget=forms.TextInput())
    recordedDate = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2023)))
    releasedDate = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2023)))
    genre = forms.CharField(widget=forms.TextInput())
    producer= forms.CharField(widget=forms.TextInput())
    composer = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = Single
        fields = ['singleName', 'recordedDate', 'releasedDate', 'genre', 'producer', 'composer']