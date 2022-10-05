from . import views
from django.urls import path

app_name ='registration'

urlpatterns =[
    path('', views.HomeView.as_view(),name='index'), #127.0.0.1/registration/
    path('createArtist', views.ArtistView.as_view(), name='createNewArtist'),
    path('createSinger', views.SingerView.as_view(), name='createNewSinger'),
    path('createActor', views.ActorView.as_view(), name='createNewActor'),
    path('createSingerActor', views.SingerActorView.as_view(), name='createNewSingerActor'),
    path('createSolo', views.SoloArtistView.as_view(), name='createNewSoloArtist'),
    path('createGroup', views.GroupArtistView.as_view(), name='createNewGroupArtist'),
    path('createSoloGroup', views.SoloArtistView.as_view(), name='createNewSoloGroupArtist'),
]