from django.urls import path
from .views import *
from django.contrib.auth import views as auth_view

app_name= 'subApp1'

urlpatterns = [
    path('osstem/', osstempage, name='brand_osstem_page'),
]