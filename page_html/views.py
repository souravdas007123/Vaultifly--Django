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

def report(request):
    return render(request,'page_html/report.html')

def team(request):
    return render(request,'page_html/team.html')

def clients(request):
    return render(request,'page_html/client.html')

def setting(request):
    return render(request,'page_html/setting.html')

def settingprofile(request):
    return render(request,'page_html/setting_profile.html')

def support(request):
    return render(request,'page_html/support.html')    