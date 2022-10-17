from . import views
from django.urls import path

app_name = 'held'

urlpatterns = [
    path('addConcert', views.ConcertView.as_view(), name='addNewConcert'),
]