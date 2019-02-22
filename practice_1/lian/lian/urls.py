"""lian URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import HttpResponse,render
import datetime
from login import views

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^login/',views.login),
    url(r'^register/',views.register),
    url(r'^ssss/',views.verify),
    url(r'^index/',views.index),
    url(r'^zhuxiao/',views.zhuxiao),

#     详细数据
    url(r'^list_jiaoce/',views.list_jiaoce),
    url(r'^list_mpvce/',views.list_mpvce),
    url(r'^list_paoce/',views.list_paoce),
    url(r'^list_pikamianbo/',views.list_pikamianbo),
    url(r'^list_xingnengyuan/',views.list_xingnengyuan),
    url(r'^list_yueyece/',views.list_yueyece),


    # 个人
    url(r'user_info/',views.geren),
    url(r'user_info1/',views.geren1),
    url(r'user_info2/',views.geren2),
    url(r'^$',views.jing),

]
