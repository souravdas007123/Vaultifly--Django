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

def inventoryoverview(request):
    return render(request,'page_html/inventory_overview.html')

def inventorysummery(request):
    return render(request,'page_html/inventory_summery.html')

def inventorystock(request):
    return render(request,'page_html/inventory_stock.html')

def inventoryproduct(request):
    return render(request,'page_html/inventory_product.html')

def inventorypurchase(request):
    return render(request,'page_html/inventory_purchase.html')

def inventorysale(request):
    return render(request,'page_html/inventory_sale.html')

def inventoryreturn(request):
    return render(request,'page_html/inventory_return.html')

def inventorybilling(request):
    return render(request,'page_html/inventory_billing.html')

def inventoryinput(request):
    return render(request,'page_html/inventory_input.html')

def report(request):
    return render(request,'page_html/report.html')

def team(request):
    return render(request,'page_html/team.html')

def teamoverviews(request):
    return render(request,'page_html/team_overview.html')

def teamlistviews(request):
    return render(request,'page_html/team_list_views.html')

def teamadd(request):
    return render(request,'page_html/team_add.html')

def clients(request):
    return render(request,'page_html/client.html')

def clientsoverviews(request):
    return render(request,'page_html/client_overview.html')

def clientslistviews(request):
    return render(request,'page_html/client_list_views.html')

def clientsadd(request):
    return render(request,'page_html/client_add.html')

def suppliers(request):
    return render(request,'page_html/suppliers.html')

def suppliersoverview(request):
    return render(request,'page_html/suppliers_overview.html')

def supplierlistview(request):
    return render(request,'page_html/suppliers_list_views.html')

def supplieradd(request):
    return render(request,'page_html/suppliers_add.html')

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

def manufacture(request):
    return render(request,'page_html/manufacture.html')

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
    return render(request,'page_html/setting_preference.html')

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