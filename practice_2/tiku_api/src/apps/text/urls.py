"""
功能介绍
"""

from django.conf.urls import url
from apps.text import views

urlpatterns=[
    url(r'^puretext$', views.puretext),
]
