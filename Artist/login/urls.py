from django.urls import path

from Artist.login import views

app_name = 'login'

urlpatterns =[
    path('login', views.LoginView.as_view(), name='login'),
]