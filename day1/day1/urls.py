"""day1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from lib2to3.pgen2.token import NAME
from unicodedata import name
from django.contrib import admin
from django.urls import path , include
from app1.views import navbar , home , contact , about , view_info ,login , register
from affairs.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('' , login , name='login') ,
    path('register/' , register , name='register') ,
    path('insert1/' ,insert1 ),
    path('insert2/' ,insert2 ),
    path('select/' , select_stud ,name='Select') ,
    path('search/' ,search_stud),
    path('delete/<id>' , del_stud),
    path('update1/<id>' ,update1.as_view())  ,
    path('update2/<id>' ,update2.as_view())  ,
    path('list-tracks-generic/' ,trackList.as_view()) ,
    path('track-form/' ,trackCreate.as_view()) ,
    path('insert-track/' ,insert_track ),
    path('myapi/' , include('myapi.urls')) ,
    path('logout/' , mylogout)




]
