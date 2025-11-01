from django.urls import path
from page_html.views import home,asset,project,projectoverview,projectworkspace,finance,inventory,report,team,clients,setting,support,settingprofile,settingpassword,settingnotification,settingauthentication,forgetpassword
urlpatterns = [
    path('', home,name='home'),
    path('asset/', asset,name='asset'),
    path('project/', project,name='project'),
    path('projectoverview/', projectoverview,name='projectoverview'),
    path('projectworkspace/', projectworkspace,name='projectworkspace'),
    path('finance/', finance,name='finance'),
    path('inventory/', inventory,name='inventory'),
    path('report/', report,name='report'),
    path('team/', team,name='team'),
    path('clients/', clients,name='clients'),
    path('setting/', setting,name='setting'),
    path('settingprofile/', settingprofile,name='settingprofile'),
    path('settingpassword/', settingpassword,name='settingpassword'),
    path('forgetpassword/', forgetpassword,name='forgetpassword'),
    path('settingnotification/', settingnotification,name='settingnotification'),
    path('settingauthentication/', settingauthentication,name='settingauthentication'),
    path('support/', support,name='support'),

]
