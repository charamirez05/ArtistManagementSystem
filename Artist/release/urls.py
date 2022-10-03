from . import views
from django.urls import path

app_name = 'release'

urlpatterns = [
    path('addRelease', views.ReleaseView.as_view(), name='addNewRelease'),
]