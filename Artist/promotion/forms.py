
from django.forms import ModelForm
from django import forms

#from Artist.registration.models import Artist, Singer
from .models import Platform


class PlatformForm(ModelForm):
    platformName = forms.CharField(widget=forms.TextInput())
    yearEstablished = forms.CharField(widget=forms.TextInput())
    ranking = forms.CharField(widget=forms.NumberInput())

    class Meta:
        model = Platform
        fields = ['platformName', 'yearEstablished', 'ranking']