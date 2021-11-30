from django.urls import path
from .views import *
from django.contrib.auth import views as auth_view

app_name= 'brandApp'

urlpatterns = [

    # 브랜드 페이지
    path('Osstem/', osstem, name='osstem_page'),
    path('Dentium/', dentium, name = 'dentium_page'),
    path('Neo/', neo, name = 'neo_page'),
    path('Dio/', dio, name = 'dio_page'),
    path('Dentis/', dentis, name = 'dentis_page'),
    path('IBS/', ibs, name = 'ibs_page'),
    path('Megagen/', megagen , name = 'megagen_page'),
    path('Henry_Schein/', henry, name = 'henry_page'),
    path('Straumann', straumann, name='straumann_page'),
    path('Envista/', envista, name = 'envista_page'),
    path('Dentsply_sirona/', dentsply, name = 'dentsply_page'),
    path('Zimmer_Biomet/', zimmer, name = 'zimmer_page'),
    
]