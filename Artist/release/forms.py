from django.forms import ModelForm
from django import forms

from .models import Album, Single


class AlbumForm(ModelForm):
    albumName = forms.CharField(widget=forms.TextInput())

    releasedDate = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2023)))
    genreList = (('KP', 'KPop'), ('P', 'Pop'), ('HHR', 'Hip-Hop Rap'), ('C', 'Country'),
                 ('RB', 'Rhythm and Blues'), ('F', 'Folk'), ('J', 'Jazz'), ('HM', 'Heavy Metal'),
                 ('EDM', 'Electronic Dance Music'), ('S', 'Soul'), ('F', 'Funk'), ('R', 'Reggae'),
                 ('D', 'Disco'), ('PR', 'Punk Rock'), ('CL', 'Classical'), ('H', 'House'),
                 ('T', 'Techno'), ('IR', 'Indie Rock'), ('G', 'Grunge'), ('A', 'Ambient'),
                 ('R', 'Reggae'), ('S', 'Soul'), ('F', 'Funk'), ('R', 'Reggae'), ('G', 'Gospel'),
                 ('LM', 'Latin Music'), ('GM', 'Grime'), ('T', 'Trap'), ('PK', 'Psychedelic Rock'))
    genre = forms.MultipleChoiceField(choices=genreList)
    dateRecorded = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2023)))

    class Meta:
        model = Album
        fields = ['albumName', 'releasedDate', 'genre', 'dateRecorded']



class SinglesForm(ModelForm):
    singleName = forms.CharField(widget=forms.TextInput())
    recordedDate = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2023)))
    releasedDate = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2023)))
    genreList = (('KP', 'KPop'), ('P', 'Pop'), ('HHR', 'Hip-Hop Rap'), ('C', 'Country'),
                 ('RB', 'Rhythm and Blues'), ('F', 'Folk'), ('J', 'Jazz'), ('HM', 'Heavy Metal'),
                 ('EDM', 'Electronic Dance Music'), ('S', 'Soul'), ('F', 'Funk'), ('R', 'Reggae'),
                 ('D', 'Disco'), ('PR', 'Punk Rock'), ('CL', 'Classical'), ('H', 'House'),
                 ('T', 'Techno'), ('IR', 'Indie Rock'), ('G', 'Grunge'), ('A', 'Ambient'),
                 ('R', 'Reggae'), ('S', 'Soul'), ('F', 'Funk'), ('R', 'Reggae'), ('G', 'Gospel'),
                 ('LM', 'Latin Music'), ('GM', 'Grime'), ('T', 'Trap'), ('PK', 'Psychedelic Rock'))

    genre = forms.MultipleChoiceField(choices=genreList)
    producer= forms.CharField(widget=forms.TextInput())
    composer = forms.CharField(widget=forms.TextInput())
    album = forms.ModelChoiceField(widget=forms.Select(),queryset=Album.objects.only('albumName'), required=False)

    class Meta:
        model = Single
        fields = ['singleName', 'recordedDate', 'releasedDate', 'genre', 'producer', 'composer', 'album']