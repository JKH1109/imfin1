from django.urls import path
from .views import *
from django.contrib.auth import views as auth_view

app_name= 'subApp1'

urlpatterns = [
    path('home/',vhome, name='thomepage'),
]