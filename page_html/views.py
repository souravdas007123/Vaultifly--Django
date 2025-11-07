from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'page_html/home.html')

def asset(request):
    return render(request,'page_html/asset.html')

def assetoverview(request):
    return render(request,'page_html/asset_overview.html')

def assetcapture(request):
    return render(request,'page_html/asset_capture.html')

def assetcapturehardwarecontain(request):
    return render(request,'page_html/asset_capture_hardware_contain.html')

def assetcapturesoftwarecontain(request):
    return render(request,'page_html/asset_capture_software_contain.html')

def assetcapturelicensecontain(request):
    return render(request,'page_html/asset_capture_license_contain.html')

def assetcapturecorelicensecontain(request):
    return render(request,'page_html/asset_capture_corelicense_contain.html')

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

def clientsviews(request):
    return render(request,'page_html/client_list_views.html')

def clientsadd(request):
    return render(request,'page_html/client_add.html')

def classification(request):
    return render(request,'page_html/classifications.html')

def classificationlocation(request):
    return render(request,'page_html/classifications_location.html')

def classificationunit(request):
    return render(request,'page_html/classifications_unit.html')

def classificationstatus(request):
    return render(request,'page_html/classifications_status.html')

def classificationcategory(request):
    return render(request,'page_html/classifications_category.html')

def setting(request):
    return render(request,'page_html/setting.html')

def settingprofile(request):
    return render(request,'page_html/setting_profile.html')

def settingpassword(request):
    return render(request,'page_html/setting_password.html')

def forgetpassword(request):
    return render(request,'page_html/forget_password.html')

def settingnotification(request):
    return render(request,'page_html/setting_notification.html')

def settingauthentication(request):
    return render(request,'page_html/setting_authentication.html')

def support(request):
    return render(request,'page_html/support.html')

def taskglobal(request):
    return render(request,'page_html/task_global.html')

def notesglobal(request):
    return render(request,'page_html/notes_global.html')

def uploadglobal(request):
    return render(request,'page_html/upload_global.html')     

def validity(request):
    return render(request,'page_html/validity.html')    