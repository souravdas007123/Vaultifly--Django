from django.urls import path
from page_html.views import home,asset,assetoverview,assetcapture,assetcapturehardwarecontain,assetcapturelicensecontain,assetcapturecorelicensecontain,assetcapturesoftwarecontain,project,projectoverview,projectworkspace,finance,inventory,report,team,clients,clientsviews,clientsadd,classification,setting,support,settingprofile,settingpassword,settingnotification,settingauthentication,forgetpassword,validity
urlpatterns = [
    path('', home,name='home'),
    path('asset/', asset,name='asset'),
    path('assetoverview/', assetoverview,name='assetoverview'),
    path('assetcapture/', assetcapture,name='assetcapture'),
    path('assetcapturehardwarecontain/', assetcapturehardwarecontain,name='assetcapturehardwarecontain'),
    path('assetcapturesoftwarecontain/', assetcapturesoftwarecontain,name='assetcapturesoftwarecontain'),
    path('assetcapturelicensecontain/', assetcapturelicensecontain,name='assetcapturelicensecontain'),
    path('assetcapturecorelicensecontain/', assetcapturecorelicensecontain,name='assetcapturecorelicensecontain'),
    path('project/', project,name='project'),
    path('projectoverview/', projectoverview,name='projectoverview'),
    path('projectworkspace/', projectworkspace,name='projectworkspace'),
    path('finance/', finance,name='finance'),
    path('inventory/', inventory,name='inventory'),
    path('report/', report,name='report'),
    path('team/', team,name='team'),
    path('clients/', clients,name='clients'),
    path('clientsviews/', clientsviews,name='clientsviews'),
    path('clientsadd/', clientsadd,name='clientsadd'),
    path('classification/', classification,name='classification'),
    path('setting/', setting,name='setting'),
    path('settingprofile/', settingprofile,name='settingprofile'),
    path('settingpassword/', settingpassword,name='settingpassword'),
    path('forgetpassword/', forgetpassword,name='forgetpassword'),
    path('settingnotification/', settingnotification,name='settingnotification'),
    path('settingauthentication/', settingauthentication,name='settingauthentication'),
    path('support/', support,name='support'),
    path('validity/', validity,name='validity'),  


]
