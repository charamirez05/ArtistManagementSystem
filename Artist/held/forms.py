from django.forms import ModelForm
from django import forms

from .models import Concert


class ConcertForm(ModelForm):
    ConcertName = forms.CharField(widget=forms.TextInput())
    VenueName = forms.CharField(widget=forms.TextInput())
    MaxParticipants = forms.IntegerField(widget=forms.NumberInput())
    ConcertDate = forms.DateField(widget=forms.SelectDateWidget(years=range(2022, 2050)))
    Location = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = Concert
        fields = ['ConcertName', 'VenueName', 'MaxParticipants', 'ConcertDate', 'Location']