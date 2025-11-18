"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # for method 1
    path('redirect1/',views.redirect_page, name='redirect_page'),
    path('home1/', views.home1, name='home1'),  
    
    # for method 2
    path('redirect2/',views.redirect2, name='redirect2'),
    path('home2/',views.home2, name='home2'),

    # for method 3(sending url with data):
    path('redirect3/',views.redirect3, name='redirect3'),
    path('home3/',views.home3, name='home3')

]
