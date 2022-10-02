from django.forms import ModelForm
from django import forms

from .models import Artist

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
        model = Artist
        fields = ['Genre', 'FandomName', 'IsSolo', 'IsGroup']


class ActorForm(ModelForm):
    nationality = forms.CharField(widget=forms.TextInput())
    #films = forms.MultiValueField(widget=forms.MultiValueField())
   # specialization = forms.MultiValueField(widget=forms.MultiValueField())

    class Meta:
        model = Artist
        fields = ['nationality']



class Charot(ModelForm):
    print("Hello World!")
    print("hello po ako po si dodong kemriel, nag tumar ug koi herbal capsule, ang ako ma istorya lang jud kay epektibo jud sya")
    print("Gusto ko nang bumitaaaaw")
    print('wag naman po!')
    print("woo to the young to the woo")

    print("Hi! Im Lynn from Las Vegas. Mowdels. Were hiring new promohtional mowdels to work en Las Vegas, Yuwezay.")
    print("eh paano kunggg??????? hindiiiii")
