from django.forms import ModelForm
from django import forms

from .models import Artist


class SingerForm(ModelForm):
    Genre = forms.CharField(widget=forms.TextInput())
    FandomName = forms.CharField(widget=forms.TextInput())
    IsSolo = forms.CharField(widget=forms.CheckboxSelectMultiple())
    IsGroup = forms.CharField(widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Artist
        fields = ['Genre', 'FandomName', 'IsSolo', 'IsGroup']


class PlatformForm(ModelForm):
    PlatformName = forms.CharField(widget=forms.TextInput())
    YearEstablished = forms.CharField(widget=forms.DateInput())
    Ranking = forms.CharField(widget=forms.NumberInput())

    class Meta:
        model = Artist
        fields = ['PlatformName', 'YearEstablished', 'Ranking']


