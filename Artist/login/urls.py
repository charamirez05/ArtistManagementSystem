from django.urls import path

from . import views

app_name = 'login'

urlpatterns =[
    path('artistlogin', views.LoginView.as_view(), name='login'),
]