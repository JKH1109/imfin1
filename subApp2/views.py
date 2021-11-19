from django.shortcuts import render

# Create your views here.
def vinfo_page(request):
    return render(request, 'Info.html')

def vinfo_manage_page(request):
    return render(request,'Manage_info.html')

def vinfo_progress_page(request):
    return render(request, 'Progress_info.html')

def vinfo_cost_page(request):
    return render(request,'Cost_info.html')
