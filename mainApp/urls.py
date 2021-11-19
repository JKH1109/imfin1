from django.urls import path , include
from .views import *

app_name = 'mainApp'

urlpatterns = [
    path('', mainPage, name='main_page'),
    path('')
    

]