# from django.urls import path
# from .views import *
# from django.contrib.auth import views as auth_view

# app_name= 'subApp1'

# urlpatterns = [
#     path('osstem/', osstempage, name='brand_osstem_page'),
# ]

from django.urls import path
from .views import *
from django.contrib.auth import views as auth_view

app_name= 'subApp1'

urlpatterns = [

    # 지역페이지
    path('Seoul/', Seoul, name='seoul_page'),
    path('Busan/',Busan, name='Busan_page'),
    path('Daegu/', Daegu, name='Daegu_page'),
    path('Daejeon/', Daejeon, name='Daejeon_page'),
    path('Sejong/', Sejong, name='Sejong_page'),
    path('Incheon/', Incheon, name='Incheon_page'),
    path('Gwangju/', Gwangju, name='Gwangju_page'),
    path('Ulsan/', Ulsan, name='Ulsan_page'),
    path('Gg', Gg, name='Gg_page'),
    path('Gangwon/', Gangwon, name='Gangwon_page'),
    path('Chungbuk/', Chungbuk, name='Chungbuk_page'),
    path('Chungnam/', Chungnam, name='Chungnam_page'),
    path('Gb/', Gb, name='Gb_page'),
    path('Gn/', Gn, name='Gn_page'),
    path('Jb/', Jb, name='Jb_page'),
    path('Jn/', Jn, name='Jn_page'),
    path('Jeju/', Jeju, name='Jeju_page'),
]