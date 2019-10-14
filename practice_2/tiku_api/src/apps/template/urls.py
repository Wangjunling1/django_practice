"""
功能介绍
"""

from django.conf.urls import url
from apps.template import views

urlpatterns=[
    url(r'^wrapper', views.render_data),
]
