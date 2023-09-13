"""
URL configuration for chanukyaproject project.

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
from chanukyasepapp.views import *
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path('home/',home,name="home"),
    path('samsung/',samsung, name="samsung"),
    path('lg/',lg, name="lg"),
    path('mi/',mi, name="mi"),
    path('oneplus/', oneplus, name="oneplus"),
    path('sony/',sony, name="sony"),
    path('realme/', realme,name="realme"),
    path('toshiba/', toshiba,name="toshiba"),
    path('onida/', onida,name="onida"),
    path('panasonic/', panasonic,name="panasonic"),
    path('lloyd/', lloyd,name="lloyd"),
    path('bpl/', bpl, name="bpl"),
    path('philips/', philips,name="philips"),
    path('products/',products ,name="products"),
    path("",login_user,name="login"),
    path("register/",register,name="register"),
    path("logout/",logout_user,name="logout"),
    path("contact/",contact,name="contact"),

]
