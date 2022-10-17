from . import views
from django.urls import path

app_name = 'star'

urlpatterns = [
    path('addFilms', views.FilmView.as_view(), name='addNewFilm'),
    path('displayFilm', views.DisplayFilmView.as_view(), name='displayFilm'),
]
