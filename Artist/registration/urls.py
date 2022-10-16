from . import views as view
from django.urls import path

app_name ='registration'

urlpatterns =[
    path('', view.HomeView.as_view(), name='index'),  # 127.0.0.1/registration/

    path('createSinger', view.SingerRegistrationView.as_view(), name='createNewSinger'),
    path('createActor', view.ActorRegistrationView.as_view(), name='createNewActor'),

    path('login', view.LoginView.as_view(), name='login'),


]