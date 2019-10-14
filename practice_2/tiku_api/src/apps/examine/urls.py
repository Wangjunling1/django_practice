"""
功能介绍
"""

from django.conf.urls import url
from apps.examine import views

urlpatterns=[
    url(r'^checkout$',views.checkout),
]
