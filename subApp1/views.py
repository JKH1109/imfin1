

from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
# Create your views here.

def osstempage(request):
    return render(request,'location/Osstem.html')

def Seoul(request):
    seoul = DB.objects.filter(지역='서울')
    return render(request,'location/Seoul.html',{'seoul':seoul})

def Busan(request):
    busan = DB.objects.filter(지역='부산')
    return render(request,'location/Busan.html',{'busan':busan})

def Daegu(request):
    daegu = DB.objects.filter(지역='대구')
    return render(request,'location/Daegu.html',{'daegu':daegu})

def Daejeon(request):
    daejeon = DB.objects.filter(지역='대전')
    return render(request, 'location/daejeon.html', {'daejeon': daejeon})

def Sejong(request):
    sejong = DB.objects.filter(지역='세종')
    return render(request, 'location/Sejong.html', {'sejong': sejong})

def Incheon(request):
    incheon = DB.objects.filter(지역='인천')
    return render(request, 'location/Incheon.html', {'incheon': incheon})

def Gwangju(request):
    gwangju = DB.objects.filter(지역='광주')
    return render(request, 'location/Gwangju.html', {'gwangju': gwangju})

def Ulsan(request):
    ulsan = DB.objects.filter(지역='울산')
    return render(request, 'location/Ulsan.html', {'ulsan': ulsan})

def Gg(request):
    gg = DB.objects.filter(지역='경기')
    return render(request, 'location/Gg.html', {'gg': gg})

def Gangwon(request):
    gangwon = DB.objects.filter(지역='강원')
    return render(request, 'location/Gangwon.html', {'gangwon': gangwon})

def Chungbuk(request):
    chungbuk = DB.objects.filter(지역='충북')
    return render(request, 'location/Chungbuk.html', {'chungbuk': chungbuk})

def Chungnam(request):
    chungnam = DB.objects.filter(지역='충남')
    return render(request, 'location/Chungnam.html', {'chungnam': chungnam})

def Gb(request):
    gb = DB.objects.filter(지역='경북')
    return render(request, 'location/Gb.html', {'gb': gb})

def Gn(request):
    gn = DB.objects.filter(지역='경남')
    return render(request, 'location/Gn.html', {'gn': gn})

def Jb(request):
    jb = DB.objects.filter(지역='전북')
    return render(request, 'location/Jb.html', {'jb': jb})

def Jn(request):
    jn = DB.objects.filter(지역='전남')
    return render(request, 'location/Jn.html', {'jn': jn})

def Jeju(request):  
    jeju = DB.objects.filter(지역='제주')
    return render(request, 'location/Jeju.html', {'jeju': jeju})


