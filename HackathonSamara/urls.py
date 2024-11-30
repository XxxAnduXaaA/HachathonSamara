"""
URL configuration for HackathonSamara project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.routers import DefaultRouter
from rest_framework import permissions

import HackathonSamara.api.v1
from HackathonSamara.api.v1.main.views import *

#from HackathonSamara.api.v1.main.views import ListUsers






urlpatterns = [
    path('admin/', admin.site.urls),
    #path('user/', ListUsers.as_view(), name='user') #permission_classes=[IsAuthenticated])
    path('api/v1/', include('HackathonSamara.api.v1.urls')),

]
