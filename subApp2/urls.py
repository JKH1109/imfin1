from django.urls import path
from .views import *
#from django.contrib.auth import auth_view
app_name='subApp2'

urlpatterns = [
    # url 
    path('', info_page, name='info_page'),
    path('manage/', info_manage_page, name='info_manage_page'),
    path('progress/', info_progress_page, name='info_progress_page'),
    path('cost/', info_cost_page, name='info_cost_page'),
]