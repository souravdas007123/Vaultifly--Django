from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'page_html/home.html')

def asset(request):
    return render(request,'page_html/asset.html')

def project(request):
    return render(request,'page_html/project.html')

def projectoverview(request):
    return render(request,'page_html/project_overview.html')

def projectworkspace(request):
    return render(request,'page_html/project_workspace.html')

def finance(request):
    return render(request,'page_html/finance.html')

def inventory(request):
    return render(request,'page_html/inventory.html')