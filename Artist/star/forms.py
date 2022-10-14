from django.forms import ModelForm
from django import forms

from .models import Film


class FilmForm(ModelForm):
    filmname = forms.CharField(widget=forms.TextInput())
    dateRelease = forms.DateField()
    actorRole = forms.CharField(widget=forms.TextInput())
    director = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = Film
        fields = ['filmname','dateRelease','actorRole','director']