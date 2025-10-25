from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'page_html/home.html')

def asset(request):
    return render(request,'page_html/asset.html')

def project(request):
    return render(request,'page_html/project.html')