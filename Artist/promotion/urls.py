from . import views
from django.urls import path

app_name = 'promotion'

urlpatterns = [
   path('addPlatform', views.PlatformView.as_view(), name='addNewPlatform'),
   path('displayPlatform', views.DisplayPlatformView.as_view(), name='displayPlatform'),
]
