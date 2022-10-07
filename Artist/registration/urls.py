from Artist.registration import views as rview
from Artist.login import views as lview
from django.urls import path

app_name ='registration'
app_name = 'login'

urlpatterns =[
    path('', rview.HomeView,name='index'), #127.0.0.1/registration/
    path('login', lview.LoginView, name='login'),
    '''path('createArtist', rview.ArtistView.as_view(), name='createNewArtist'),
    path('createSinger', rview.SingerView.as_view(), name='createNewSinger'),
    path('createActor', rview.ActorView.as_view(), name='createNewActor'),
    path('createSingerActor', rview.SingerActorView.as_view(), name='createNewSingerActor'),
    path('createSolo', rview.SoloArtistView.as_view(), name='createNewSoloArtist'),
    path('createGroup', rview.GroupArtistView.as_view(), name='createNewGroupArtist'),
    path('createSoloGroup', rview.SoloArtistView.as_view(), name='createNewSoloGroupArtist'),'''
]