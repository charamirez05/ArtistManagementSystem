from django.forms import forms, ModelForm
from django import forms


from .models import Artist, Singer, Actor


class SingerForm(ModelForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    ArtistName = forms.CharField(widget=forms.TextInput())
    YearsActive = forms.CharField(widget=forms.NumberInput())
    birthDate = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2023)))
    debutDate = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2023)))
    isSinger = forms.BooleanField(widget = forms.HiddenInput(), required=False, initial=True)
    genreList = (('KP', 'KPop'), ('P', 'Pop'), ('HHR', 'Hip-Hop Rap'), ('C', 'Country'),
                 ('RB', 'Rhythm and Blues'), ('F', 'Folk'), ('J', 'Jazz'), ('HM', 'Heavy Metal'),
                 ('EDM', 'Electronic Dance Music'), ('S', 'Soul'), ('F', 'Funk'), ('R', 'Reggae'),
                 ('D', 'Disco'), ('PR', 'Punk Rock'), ('CL', 'Classical'), ('H', 'House'),
                 ('T', 'Techno'), ('IR', 'Indie Rock'), ('G', 'Grunge'), ('A', 'Ambient'),
                 ('R', 'Reggae'), ('S', 'Soul'), ('F', 'Funk'), ('R', 'Reggae'), ('G', 'Gospel'),
                 ('LM', 'Latin Music'), ('GM', 'Grime'), ('T', 'Trap'), ('PK', 'Psychedelic Rock'))
    instrumentList = (('AG', 'Acoustic Guitar'), ('BJ', 'Banjo'), ('B', 'Bass'), ('CL', 'Cello'), ('C', 'Clarinet'),
                       ('EG', 'Electric Guitar'), ('D', 'Drums'), ('F', 'Flute'), ('PKO', 'Piano/Keyboard/Organ'),
                      ('S', 'Saxophone'),  ('T', 'Trumpet'),  ('U', 'Ukelele'), ('V', 'Voice only'), ('V', 'Violin'))

    Instruments = forms.MultipleChoiceField(choices=instrumentList)
    Genre = forms.MultipleChoiceField(choices=genreList)
    FandomName = forms.CharField(widget=forms.TextInput())


    class Meta:
        model = Singer
        fields = ['username', 'password', 'ArtistName', 'YearsActive', 'birthDate', 'debutDate', 'Genre', 'FandomName', 'Instruments', 'isSinger']


class ActorForm(ModelForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    ArtistName = forms.CharField(widget=forms.TextInput())
    YearsActive = forms.CharField(widget=forms.NumberInput())
    birthDate = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2023)))
    debutDate = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2023)))
    isActor = forms.BooleanField(widget=forms.HiddenInput(), required=False, initial=True)
    specializationList = (('T', 'Theatre Acting'), ('TV', 'TV Acting'), ('F', 'Film Acting'),
                          ('VO', 'Voice Over Acting'), ('C', 'Commercials Acting'), ('EB', 'Extra/Background Acting'))
    specialization = forms.MultipleChoiceField(choices=specializationList)
    nationality = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = Actor
        fields = ['username', 'password', 'ArtistName', 'YearsActive', 'birthDate', 'debutDate', 'nationality', 'specialization', 'isActor']

