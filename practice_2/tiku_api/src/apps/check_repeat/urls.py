"""
功能介绍
"""

from django.conf.urls import url
from apps.check_repeat import views

urlpatterns=[
    url(r'^detection',views.Detection.as_view(),name='detection'),
]
