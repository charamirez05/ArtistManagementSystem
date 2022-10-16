from django.forms import ModelForm
from django import forms

#from Artist.registration.models import Artist, Singer
from .models import Platform


class PlatformForm(ModelForm):
    PlatformName = forms.CharField(widget=forms.TextInput())
    YearEstablished = forms.CharField(widget=forms.TextInput())
    Ranking = forms.CharField(widget=forms.NumberInput())

    class Meta:
        model = Platform
        fields = ['PlatformName', 'YearEstablished', 'Ranking']


