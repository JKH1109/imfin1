from django.shortcuts import render

# Create your views here.

#오스템
def osstem(request):
    return render(request, 'Osstem.html')
#덴티움
def dentium(request):
    return render(request, 'Dentium.html')
#네오
def neo(request):
    return render(request, 'Neo.html')
#디오
def dio(request):
    return render(request, 'Dio.html')
#덴티스
def dentis(request):
    return render(request, 'Dentis.html')
#IBS
def ibs(request):
    return render(request, 'IBS.html')
#헨리슈헨    
def henry(request):
    return render(request, 'Henry_Schein.html')
#스트라우만    
def straumann(request):
    return render(request, 'Straumann.html')


#엔비스타    
def envista(request):
    return render(request, 'Envista.html')
#덴츠플라이
def dentsply(request):
    return render(request, 'Dentsply_Sirona.html')
#지머바이오멧
def zimmer(request):
    return render(request, 'Zimmer_Biomet.html')
#메가젠
def megagen(request):
    return render(request, 'Megagen.html')
