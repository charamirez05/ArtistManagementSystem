from django.forms import ModelForm
from django import forms

from .models import Platform


class PlatformForm(ModelForm):
    PlatformName = forms.CharField(widget=forms.TextInput())
    YearEstablished = forms.CharField(widget=forms.DateInput())
    Ranking = forms.CharField(widget=forms.NumberInput())

    class Meta:
        model = Platform
        fields = ['PlatformName', 'YearEstablished', 'Ranking']


