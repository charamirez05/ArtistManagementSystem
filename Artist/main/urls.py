from . import views as view
from django.urls import path

app_name ='main'

urlpatterns =[
    path('', view.HomeView.as_view(), name='index'),  # 127.0.0.1/main/
]