from . import views as view
from django.urls import path

app_name ='registration'

urlpatterns =[
    path('', view.HomeView.as_view(), name='index'),  # 127.0.0.1/registration/
    path('createArtist', view.ArtistView.as_view(), name='createNewArtist'),
    path('createSinger', view.SingerView.as_view(), name='createNewSinger'),
    path('createActor', view.ActorView.as_view(), name='createNewActor'),
    path('createSingerActor', view.SingerActorView.as_view(), name='createNewSingerActor'),
    path('createSolo', view.SoloArtistView.as_view(), name='createNewSoloArtist'),
    path('createGroup', view.GroupArtistView.as_view(), name='createNewGroupArtist'),
    path('createSoloGroup', view.SoloArtistView.as_view(), name='createNewSoloGroupArtist'),
]