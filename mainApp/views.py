from django.shortcuts import render

# Create your views here.
def mainPage(request):
    return render(request,'Home.html')

# def base(request):
#     return render(request,'base.html')

# def infopage(request):
#     return render(request, "Info.html")

# def costinfo(request):
#     return render(request, '')