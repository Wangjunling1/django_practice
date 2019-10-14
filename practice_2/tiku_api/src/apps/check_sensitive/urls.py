"""
功能介绍
"""

from django.conf.urls import url
from apps.check_sensitive import views

urlpatterns=[
    url(r'^sensitive',views.sensitive),
]
