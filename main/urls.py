from django.urls import path
from . import views


urlpatterns =[
    path('',views.home,name='home'),
    # path('topPages/',views.personalityType,name='toppages'),
    path('taketest/',views.personalityTest,name='taketest'),
    path('allProfiles/',views.AllProfiles,name='allProfiles'),
    path('about/',views.aboutpage,name='about'),
]   