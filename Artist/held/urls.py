from . import views
from django.urls import path

app_name = 'held'

urlpatterns = [
    path('addNewConcert', views.ConcertView.as_view(), name='addNewConcert'),
    path('displayConcert', views.DisplayConcert.as_view(), name='displayConcert')
]
