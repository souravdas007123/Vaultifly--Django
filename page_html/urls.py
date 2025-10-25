from django.urls import path
from page_html.views import home,asset,project
urlpatterns = [
    path('', home,name='home'),
    path('asset/', asset,name='asset'),
    path('project/', project,name='project'),

]
