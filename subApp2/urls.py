from django.urls import path
from .views import *
#from django.contrib.auth import auth_view
app_name='subApp2'

urlpatterns = [
    # url 
    path('', vinfo_page, name='tinfo_page'),
    path('manage/', vinfo_manage_page, name='tinfo_manage_page'),
    path('progress/', vinfo_progress_page, name='tinfo_progress_page'),
    path('cost/', vinfo_cost_page, name='tinfo_cost_page'),
]