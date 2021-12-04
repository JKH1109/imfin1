from django.urls import path
from .views import *
#from django.contrib.auth import auth_view
app_name='subApp2'

urlpatterns = [
    #Example info 
    path('', info_page, name='info_page'),
    #Example info/manage/
    path('manage/', info_manage_page, name='info_manage_page'),
    #Example info/progress/
    path('progress/', info_progress_page, name='info_progress_page'),
    #Example info/cost/
    path('cost/', info_cost_page, name='info_cost_page'),

    #Example info/City/
    path('City/', info_city_page, name = 'info_city_page'),
    #Example info/Hospital/
    path('Hostpital/', info_hospital_page, name='info_hospital_page'),
    
]