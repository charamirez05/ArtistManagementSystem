from . import views
from django.urls import path

app_name = 'release'

urlpatterns = [
    path('addAlbumRelease', views.AlbumView.as_view(), name='addNewAlbumRelease'),
    path('addSinglesRelease', views.SinglesView.as_view(), name='addNewSinglesRelease'),
    path('displayAlbum', views.DisplayAlbumView.as_view(), name='displayAlbum'),
    path('displaySingle', views.DisplaySingleView.as_view(), name='displaySingle'),
]
