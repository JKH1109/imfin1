from django.urls import path , include
from .views import *

app_name = 'mainApp'

urlpatterns = [
    path('', mainPage, name='main_page'),

    
    #인증 URL 3개 추가
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', UserCreateView.as_view(), name='register'),
    path('accounts/register/done/', UserCreateDoneTV.as_view(), name='register_done'),
]   