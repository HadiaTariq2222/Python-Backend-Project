"""
URL configuration for Authentication project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from main.views import *
urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('home/', home_page, name='home_page'),
    path('home/login/', login_page, name='login_page'),
    path('home/register/', register_page, name='register_page'),
    path('home/success/', success_page, name='success_page'),
    path('verify/<auth_token>' , verify , name="verify"),
    path('home/register/token_send/', token_send_page, name='token_send'),
    path('home/register/error/', error, name='error'),
]
